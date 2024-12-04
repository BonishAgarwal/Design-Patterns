from stripe_payment import StripePayment
from payment_adapter import PaymentAdapter


def main():
    adapter = PaymentAdapter(StripePayment())
    
    adapter.process_payment()


if __name__ == "__main__":
    main()