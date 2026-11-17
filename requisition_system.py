#BACT7501 Assignment 2
#Purchase requisition system
#Initial project setup

requisition_counter = 10000

class Requisition:
    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        global requisition_counter
        requisition_counter += 1
        self.requisition_id = requisition_counter
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
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three
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
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three

        elif decision == "Not approved":
            self.status = "Not approved"
            self.approval_reference = ""

        else:
            print("Invalid decision. Requisition remains pending.")

        return self.status

    def display_requisitions(self):
        print("\n-----------------------------")
        print("PURCHASE REQUISITION DETAILS")
        print("-----------------------------")

        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print(f"Total: ${self.total:.2f}")
        print("Status:", self.status)

        if self.approval_reference:
            print("Approval Reference Number:",
                    self.approval_reference)
        else:
            print("Approval Reference Number: Not available")

        print("-----------------------------")

    def requisition_statistics(self, requisitions):
        total = len(requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            elif requisition.status == "Not approved":
                not_approved += 1

        print("\nREQUISITION STATISTICS")
        print("Total Requisitions:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not Approved:", not_approved)

        return total, approved, pending, not_approved


request1 = Requisition("17/11/2026", "FN19", "John Paul")

request1.add_requisition("Keyboard", 100)
request1.add_requisition("Mouse", 50)
request1.add_requisition("Monitor", 300)

print("Final Total:", request1.total)
print("Staff Name:", request1.staff_name)
print("Staff ID:", request1.staff_id)
print("Status:", request1.status)

request1.approve_requisition()

print("Requisition ID:", request1.requisition_id)
print("Approval Status:", request1.status)
print("Approval Reference:", request1.approval_reference)

request2 = Requisition("17/11/2026", "FN20", "Tracy Brown")
request2.add_requisition("Laptop", 1000)
request2.approve_requisition()

print("Before Manager Decision:", request2.status)

request2.respond_requisition("Approved")

print("After Manager Decision:", request2.status)
print("Approval Reference:", request2.approval_reference)

request1.display_requisitions()
request2.display_requisitions()

# Third requisition
request3 = Requisition("17/11/2026", "FN21", "Sarah Lee")
request3.add_requisition("Printer", 800)
request3.approve_requisition()
request3.respond_requisition("Not approved")

# Fourth requisition
request4 = Requisition("17/11/2026", "FN22", "David Kim")
request4.add_requisition("Office Chair", 300)
request4.approve_requisition()

# Fifth requisition
request5 = Requisition("17/11/2026", "FN23", "Emma Wilson")
request5.add_requisition("Projector", 1500)
request5.approve_requisition()

all_requisitions = [
    request1,
    request2,
    request3,
    request4,
    request5
]
request1.requisition_statistics(all_requisitions)

# Final testing of all requisitions

print("\nFINAL REQUISITION RESULTS")

for request in all_requisitions:
    request.display_requisitions()

print("\nFINAL STATISTICS")
request1.requisition_statistics(all_requisitions)

print("\nCHECKING REQUISITION IDS")

for request in all_requisitions:
    print(request.requisition_id)

print("\nCHECKING APPROVAL REFERENCES")

for request in all_requisitions:
    print(
        request.requisition_id,
        request.status,
        request.approval_reference
    )

request1.requisition_statistics(all_requisitions)




