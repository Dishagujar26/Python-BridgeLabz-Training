# Python doesn't enforce access control like Java/C++.
# Instead, it uses NAMING CONVENTIONS to signal intent.
# There are 3 levels: Public, Protected, and Private.

class BankAccount:

    # 1. PUBLIC (no underscore prefix)
    # Accessible from anywhere — inside or outside the class. This is the default for all attributes and methods.
   
    def __init__(self, owner, balance):
        self.owner = owner           # public  → freely accessible
        self._bank_name = "PyBank"   # protected
        self.__balance = balance     # private

    def deposit(self, amount):       # public method
        """Anyone can call this method."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    # 2. PROTECTED (single underscore prefix: _name)
    # Convention: "internal use — handle with care."
    # Python does NOT enforce this — it's a GENTLEMAN'S AGREEMENT.
    # Accessible from outside, but you're saying "please don't."
    # Commonly used in base classes meant to be subclassed.
   
    def _calculate_interest(self):   # protected method
        """Intended for internal/subclass use only."""
        return self.__balance * 0.05

    # 3. PRIVATE (double underscore prefix: __name)
    # Python applies NAME MANGLING: __attr becomes _ClassName__attr
    # This makes accidental override/access harder (not impossible).
    # Use to protect critical internal state from external mutation.

    def __validate_withdrawal(self, amount):  # private method
        """Only this class should call this."""
        return 0 < amount <= self.__balance

    def withdraw(self, amount):      # public — acts as a safe interface
        if self.__validate_withdrawal(amount):
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):           # public getter for private data
        return self.__balance



acc = BankAccount("Rahul", 10000)

# PUBLIC — works perfectly fine
print(acc.owner)                     # → Rahul
acc.deposit(2000)                    # → Deposited ₹2000. New balance: ₹12000
acc.withdraw(500)                    # → Withdrawn ₹500. Balance: ₹11500
print(acc.get_balance())             # → 11500

# PROTECTED — accessible, but discouraged outside class/subclass
print(acc._bank_name)                # → PyBank  (works, but bad practice)
print(acc._calculate_interest())     # → 575.0   (works, but bad practice)

# PRIVATE — direct access is blocked by name mangling
# print(acc.__balance)                   # → AttributeError!
# print(acc.__validate_withdrawal(100))  # → AttributeError!

# Name mangling: Python renames __balance to _BankAccount__balance
# You CAN still access it this way (Python doesn't truly hide it):
print(acc._BankAccount__balance)     # → 11500  (but NEVER do this!)


# inheritance with access modifiers 

class SavingsAccount(BankAccount):

    def show_details(self):
        # Public — accessible in subclass
        print(f"Owner: {self.owner}")

        # Protected — accessible in subclass (intended use)
        print(f"Bank: {self._bank_name}")
        print(f"Interest: ₹{self._calculate_interest()}")

        # Private — NOT accessible in subclass (name-mangled)
        # print(self.__balance)      # → AttributeError!

        # Use the public getter instead
        print(f"Balance: ₹{self.get_balance()}")


sav = SavingsAccount("Priya", 50000)
sav.show_details()