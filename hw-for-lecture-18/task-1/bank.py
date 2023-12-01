import unittest
from unittest.mock import patch
import io


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        if self.balance > 0:
            interest_amount = self.balance * (self.interest_rate / 100)
            self.balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < 0:
            return f"Overdraft letter sent for Account {self.account_number}"


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed.")

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts:
            print(account)


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(account_number=123456, balance=1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw_sufficient_balance(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.balance, 700.0)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500.0)

    def test_str(self):
        self.assertEqual(str(self.account), "Account 123456: Balance $1000.00")


class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.savings_account = SavingsAccount(
            account_number=654321, balance=2000.0, interest_rate=5.0
        )

    def test_add_interest(self):
        self.savings_account.add_interest()
        expected_balance = 2000.0 + (2000.0 * 0.05)
        self.assertEqual(self.savings_account.balance, expected_balance)

    def test_add_interest_zero_balance(self):
        zero_balance_account = SavingsAccount(
            account_number=123456, balance=0.0, interest_rate=3.0
        )
        zero_balance_account.add_interest()
        self.assertEqual(zero_balance_account.balance, 0.0)

    def test_add_interest_negative_balance(self):
        negative_balance_account = SavingsAccount(
            account_number=567890, balance=-500.0, interest_rate=2.5
        )
        negative_balance_account.add_interest()
        self.assertEqual(negative_balance_account.balance, -500.0)


class TestCurrentAccount(unittest.TestCase):
    def setUp(self):
        self.current_account = CurrentAccount(
            account_number=123456, balance=500.0, overdraft_limit=1000.0
        )

    def test_send_overdraft_letter_positive_balance(self):
        result = self.current_account.send_overdraft_letter()
        self.assertIsNone(result)

    def test_send_overdraft_letter_negative_balance_within_limit(self):
        self.current_account.balance = -200.0
        result = self.current_account.send_overdraft_letter()
        expected_output = "Overdraft letter sent for Account 123456"
        self.assertEqual(result, expected_output)

    def test_send_overdraft_letter_negative_balance_exceed_limit(self):
        self.current_account.balance = -1200.0
        result = self.current_account.send_overdraft_letter()
        expected_output = "Overdraft letter sent for Account 123456"
        self.assertEqual(result, expected_output)


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

        self.savings_account = SavingsAccount(
            account_number=123456, balance=1000.0, interest_rate=5.0
        )
        self.current_account = CurrentAccount(
            account_number=456789, balance=500.0, overdraft_limit=1000.0
        )

    def test_open_account(self):
        self.bank.open_account(self.savings_account)
        self.assertIn(self.savings_account, self.bank.accounts)

    def test_close_account(self):
        self.bank.open_account(self.current_account)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.bank.close_account(self.current_account.account_number)
            self.assertEqual(mock_stdout.getvalue(), "Account 456789 closed.\n")
            self.assertNotIn(self.current_account, self.bank.accounts)

    def test_close_account_nonexistent(self):
        self.assertEqual(self.bank.close_account(234567), None)

    def test_pay_dividend(self):
        self.bank.open_account(self.savings_account)
        self.bank.open_account(self.current_account)
        self.bank.pay_dividend(200.0)
        expected_savings_balance = 1000.0 + 200.0
        expected_current_balance = 500.0 + 200.0
        self.assertEqual(self.savings_account.balance, expected_savings_balance)
        self.assertEqual(self.current_account.balance, expected_current_balance)

    def test_update_accounts(self):
        self.bank.open_account(self.savings_account)
        self.bank.open_account(self.current_account)
        with patch.object(
            SavingsAccount, "add_interest"
        ) as mock_add_interest, patch.object(
            CurrentAccount, "send_overdraft_letter"
        ) as mock_send_overdraft_letter:
            self.bank.update_accounts()
            mock_add_interest.assert_called_once()
            mock_send_overdraft_letter.assert_called_once()

    def test_show_accounts(self):
        self.bank.open_account(self.savings_account)
        self.bank.open_account(self.current_account)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.bank.show_accounts()
            expected_output = (
                "Account 123456: Balance $1000.00\n" "Account 456789: Balance $500.00\n"
            )
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
