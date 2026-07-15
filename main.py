import config
from core_manager import check_update_policy, check_beta_slots

def main():
    print("============================================")
    print(f" SYSTEM INITIALIZATION: {config.APP_NAME}")
    print(f" VERSION: {config.VERSION}")
    print(" STATUS: SECURE | ENTERPRISE MODE ACTIVE")
    print("============================================")
    
    app = "com.whatsapp"
    policy = check_update_policy(app)
    beta = check_beta_slots(100)
    
    print(f"[PROCESS] Checking Package: {app}")
    print(f"[RESULT] Policy Applied: {policy}")
    print("--------------------------------------------")
    print(f"[STATUS] Beta Enrollment: {beta}")
    print("============================================")
    print("SYSTEM READY FOR DEPLOYMENT")

if __name__ == "__main__":
    main()
