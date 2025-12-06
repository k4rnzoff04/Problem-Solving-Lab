inventory = {
    1000: 2,
    500: 5,
    100: 10,
    50: 10,
    20: 20,
    10: 30,
    5: 20,
    2: 50,
    1: 0
}

DENOMS = sorted(inventory.keys(), reverse=True)

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def calculate_change(change, inventory):
    result = []

    for denom in DENOMS:
        if change == 0:
            break

        count_needed = change // denom
        count_available = inventory[denom]
        count_to_use = min(count_needed, count_available)

        if count_to_use > 0:
            result.append((denom, count_to_use))
            change -= denom * count_to_use
            inventory[denom] -= count_to_use

    # change เหลือเท่าไร นั่นคือยอดที่ทอนไม่ได้
    return result, change

def print_breakdown(change_list):
    print("\nรายละเอียดการทอนเงิน:")
    total = 0
    for denom, count in change_list:
        subtotal = denom * count
        total += subtotal
        print(f"{denom} x {count} = {subtotal}")
    print("จำนวนเงินที่ทอนไป:", total)

product_price = get_int_input("Enter product price: ")

while True:
    paid = get_int_input("Enter paid amount: ")
    change = paid - product_price

    if change < 0:
        print(f"ยอดชำระไม่พอ ต้องการเพิ่มอีก {product_price - paid} บาท.")
    else:
        break

if change == 0:
    print("ชำระครบจำนวน ไม่ต้องทอน.")
else:
    print(f"\nจำนวนที่ต้องทอน = {change}")

    result, remaining = calculate_change(change, inventory)

    if remaining > 0:
        print("\n‼ สต็อกเหรียญ/ธนบัตรไม่เพียงพอ ทอนไม่ครบ ‼")
        print(f"ยอดคงเหลือที่ไม่ได้ทอน: {remaining}")

    print_breakdown(result)
