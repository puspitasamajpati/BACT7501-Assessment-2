#BACT7501 Assignment 2
#Purchase requisition system
#Initial project setup
class Requisition:
    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = None
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = ""

    def add_requisition(self, item_name, item_price):
        item = {
            "name": item_name,
            "price": item_price
        }

        self.items.append(item)
        self.total += item_price

        print("Item added:", item_name)
        print(f"Current Total: ${self.total:.2f}")

        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)
            )
        else:
            self.status = "Pending"
            self.approval_reference = ""

        return self.status

    def respond_requisition(self, decision):
        if self.status != "Pending":
            print("This requisition is already processed.")
            return self.status

        if decision == "Approved":
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)
            )

        elif decision == "Not approved":
            self.status = "Not approved"
            self.approval_reference = ""

        else:
            print("Invalid decision. Requisition remains pending.")

        return self.status


# Testing the requisition system
request1 = Requisition("17/11/2026", "FN19", "John Paul")

request1.add_requisition("Keyboard", 100)
request1.add_requisition("Mouse", 50)
request1.add_requisition("Monitor", 300)

print("Final Total:", request1.total)
print("Staff Name:", request1.staff_name)
print("Staff ID:", request1.staff_id)
print("Status:", request1.status)

request1.requisition_id = 10001

request1.approve_requisition()

print("Requisition ID:", request1.requisition_id)
print("Approval Status:", request1.status)
print("Approval Reference:", request1.approval_reference)

request2 = Requisition("17/11/2026", "FN20", "Tracy Brown")
request2.requisition_id = 10002

request2.add_requisition("Laptop", 1000)
request2.approve_requisition()

print("Before Manager Decision:", request2.status)

request2.respond_requisition("Approved")

print("After Manager Decision:", request2.status)
print("Approval Reference:", request2.approval_reference)

