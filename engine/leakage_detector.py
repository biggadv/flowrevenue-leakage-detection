def detect_revenue_leakage(expected_revenue, actual_revenue):
    leaks = []

    for contract_id, expected_value in expected_revenue.items():
        actual_value = actual_revenue.get(contract_id, 0)

        if actual_value < expected_value:
            leaks.append({
                "contract_id": contract_id,
                "expected": expected_value,
                "actual": actual_value,
                "leakage": expected_value - actual_value
            })

    return leaks
