


# def human_verification_node(state):
#     stock = state["investment_instruments"][0]
#     print("\nHuman Verification Required:")
#     print(f"Suggested Stock: {stock['tradingsymbol']} at ₹{stock['price']}")
#     decision = input("Do you approve this purchase? (yes/no): ").strip().lower()
#     state["approved"] = decision in ["yes", "y"]
#     print(f"DEBUG in Human apprval: approved={state['approved']}")
#     return state


# human_approval.py
# def human_verification_node(state):
#     """
#     Human verification node for the graph.
#     Server sets state['approved'] = True/False to control approval.
#     """
#     stock = state.get("investment_instruments", [{}])[0]
#
#     print("\nHuman Verification Required:")
#     print(f"Suggested Stock: {stock.get('tradingsymbol', 'N/A')} at ₹{stock.get('price', 'N/A')}")
#
#     # If approval is not yet set by server, default to False
#     if "approved" not in state or state["approved"] is None:
#         state["approved"] = False
#         print("DEBUG: Waiting for server/frontend to provide approval...")
#         # The graph will pause here; stock_buy_tools won't execute yet
#         return state
#
#     # Approval provided by server
#     if state["approved"]:
#         print(f"DEBUG: Human approval received: approved={state['approved']}")
#     else:
#         print("DEBUG: Purchase not approved. Stock buy will be skipped.")
#
#     return state




def human_verification_node(state):
    stock = state.get("investment_instruments", [{}])[0]

    print("\nHuman Verification Required:")
    print(f"Suggested Stock: {stock.get('tradingsymbol', 'N/A')} at ₹{stock.get('price', 'N/A')}")

    # Pause if approval not yet set
    if state.get("approved") is None:
        print("DEBUG: Waiting for server/frontend to provide approval...")
        return state  # Do NOT continue to stock_buy_tools yet

    if state["approved"]:
        print(f"DEBUG: Human approval received: approved={state['approved']}")
    else:
        print("DEBUG: Purchase not approved. Stock buy will be skipped.")

    return state


