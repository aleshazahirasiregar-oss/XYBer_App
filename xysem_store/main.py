import config
from .core_manager import check_update_policy, check_beta_slots

def main():
    print("\n" + "="*50)
    print(f" {config.APP_NAME.upper()} | VERSION: {config.VERSION}")
    print("="*50)
    
    # Simulasi testing dengan error handler
    apps_to_test = ["com.whatsapp", 12345] 
    
    for app in apps_to_test:
        policy = check_update_policy(app)
        print(f"[*] Analyzing: {app}")
        print(f"    [Result]: {policy}")
        print("-" * 50)
        
    status = check_beta_slots(500)
    print(f"[!] Beta Enrollment: {status}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
