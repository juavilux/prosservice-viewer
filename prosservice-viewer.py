import psutil

def list_processes():
    # List all processes
    for process in psutil.process_iter(['pid', 'name', 'username']):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}")

def list_services():
    # List all services
    services = psutil.win_service_iter()
    for service in services:
        print(f"Name: {service.name()}, Display Name: {service.display_name()}, Status: {service.status()}")

def main():
    while True:
        print("\nQual você deseja visualizar?:")
        print("1. Processos")
        print("2. Serviços")
        print("3. Sair")
        
        choice = input("\nEscolha uma opção: ")
        
        if choice == "1":
            list_processes()
        elif choice == "2":
            list_services()
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
