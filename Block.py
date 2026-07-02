import protected
import inspect

# Tarmuxset ক্লাস ডিফাইন করুন (যদি protected মডিউলে না থাকে)
class Tarmuxset:
    @staticmethod
    def auto_run():
        """Auto run function"""
        print("Auto running...")
        return True

try:
    # চেক করুন auto_run মেথড আছে কিনা
    if hasattr(Tarmuxset, 'auto_run'):
        print("Auto_run arguments:", inspect.signature(Tarmuxset.auto_run))
    else:
        print("auto_run method not found")
except Exception as e:
    print(f"Signature not found: {e}")
    print("Trying main...")

# protected.main() চালানোর চেষ্টা করুন
try:
    if hasattr(protected, 'main'):
        protected.main()
    else:
        print("protected.main() not found")
except Exception as e:
    print(f"Error running protected.main(): {e}")
