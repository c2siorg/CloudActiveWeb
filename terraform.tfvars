# #########################################################################################################################################
#                                                           Terraform Variables
# #########################################################################################################################################

project = "terraform-project-339305"

vm_nodes = {
    node_01: {vm_no: 0, vm_name:"terra-ansi-instance-01"}
    node_02: {vm_no: 1, vm_name:"terra-ansi-instance-02"}
    node_03: {vm_no: 2, vm_name:"terra-ansi-instance-03"}
    node_04: {vm_no: 3, vm_name:"terra-ansi-instance-04"}
}

machine_type = "e2-standard-2"

zone = "us-east1-b"

ssh_user = "stp"

ssh_prv_key = "/home/aroshd/.ssh/stp_key"

ssh_pub_key = "/home/aroshd/.ssh/stp_key.pub"

# #########################################################################################################################################
#                                                            Ansible Variables
# #########################################################################################################################################

gcp_service_email = "t-320-283@terraform-project-339305.iam.gserviceaccount.com"

gcp_bucket = "stp-5-wb"

seed_file = "stp-5-wb-non-inset-200feed.csv"

script = "active.py"

service_account_file = "service_account.json"