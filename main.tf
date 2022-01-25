terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.90.0"
    }
  }
}

provider "google" {
  credentials = file("keys/${var.service_account_file}")
  project     = var.project
}

# #########################################################################################################################################
#                                                            Resources
# #########################################################################################################################################
resource "google_compute_instance" "vm_instance" {
  for_each = var.vm_nodes

  project = var.project

  name = each.value.vm_name

  machine_type = var.machine_type

  zone = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 10
      type  = "pd-standard"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

  metadata = {
    ssh-keys = "${var.ssh_user}:${file(var.ssh_pub_key)}"
  }

  tags = ["externalssh"]

  provisioner "remote-exec" {
    inline = ["sudo apt update", "sudo apt -y install python3-pip"]

    connection {
      type = "ssh"

      port = 22

      user = var.ssh_user

      host = self.network_interface[0].access_config[0].nat_ip

      private_key = file(var.ssh_prv_key)

      timeout = "5m"
    }
  }

  provisioner "local-exec" {
    command = "ansible-playbook --extra-vars='{\"ssh_user\": ${var.ssh_user}, \"project\": ${var.project}, \"gcp_service_email\": ${var.gcp_service_email}, \"vm_name\": ${each.value.vm_name}, \"vm_no\": ${each.value.vm_no}, \"seed_file\": ${var.seed_file}, \"script\": ${var.script}, \"gcp_bucket\": ${var.gcp_bucket}, \"service_account_file\": ${var.service_account_file}}' -i '${self.network_interface[0].access_config[0].nat_ip},' playbook.yaml"
  }

}
