from core_manager import check_update_policy, check_beta_slots
import config

def main():
    print(f"--- Welcome to {config.APP_NAME} ---")
    
    app_to_check = "com.whatsapp"
    policy = check_update_policy(app_to_check)
    print(f"Policy for {app_to_check}: {policy}")
    
    current_beta = 100
    beta_status = check_beta_slots(current_beta)
    print(f"Beta Access Status: {beta_status}")

if __name__ == "__main__":
    main()

