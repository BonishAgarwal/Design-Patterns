from base import Subject
from email_notifier import EmailObserver


def main():
    
    # register the observer
    subject = Subject()
    subject.add_observers(EmailObserver())
    
    # notify
    subject.notify_observers()

if __name__ == "__main__":
    main()