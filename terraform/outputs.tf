output "master_public_ip" {
  value = azurerm_public_ip.master_ip.ip_address
}

output "worker_public_ip" {
  value = azurerm_public_ip.worker_ip.ip_address
}

output "master_private_ip" {
  value = azurerm_linux_virtual_machine.master.private_ip_address
}

output "worker_private_ip" {
  value = azurerm_linux_virtual_machine.worker.private_ip_address
}
