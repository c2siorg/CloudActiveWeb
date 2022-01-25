variable "project" {
  type    = string
  default = ""
}

variable "vm_nodes" {
  type    = map(any)
  default = {}
}

variable "gcp_service_email" {
  type    = string
  default = ""
}

variable "vm_name" {
  type    = string
  default = ""
}

variable "machine_type" {
  type    = string
  default = ""
}

variable "zone" {
  type    = string
  default = ""
}

variable "ssh_user" {
  type    = string
  default = ""
}

variable "ssh_pub_key" {
  type    = string
  default = ""
}

variable "ssh_prv_key" {
  type    = string
  default = ""
}

variable "gcp_bucket" {
  type    = string
  default = ""
}

variable "seed_file" {
  type    = string
  default = ""
}

variable "script" {
  type    = string
  default = "active.py"
}

variable "service_account_file" {
  type    = string
  default = "service_account.json"
}
