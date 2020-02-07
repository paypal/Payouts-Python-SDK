import time
from create_payouts import CreatePayouts
from get_payouts import GetPayouts
from get_payout_item import GetPayoutItem
from cancel_payout_item import CancelPayoutItem

print('Creating Payouts')
create_response = CreatePayouts().create_payouts(True)
if create_response.status_code == 201:
    batch_id = create_response.result.batch_header.payout_batch_id
    print('Retrieving Payouts batch with id: ' + batch_id)
    get_response = GetPayouts().get_payouts(batch_id, True)
    if get_response.status_code == 200:
        item_id = get_response.result.items[0].payout_item_id
        print('Retrieving Payout item with id: ' + item_id)
        get_item_response = GetPayoutItem().get_payout_item(item_id, True)
        if get_item_response.status_code == 200:
            print(
                'Check Payouts status to see if it has completed processing all payments')
            for i in range(5):
                time.sleep(2)
                get_response = GetPayouts().get_payouts(batch_id, True)
                if get_response.result.batch_header.batch_status == "SUCCESS":
                    print('Cancelling unclaimed payout item with id: ' + item_id)
                    cancel_response = CancelPayoutItem().cancel_payout_item(item_id, True)
                    if cancel_response.status_code == 200:
                        print(
                            'Successfully cancelled unclaimed payout item with id: ' + item_id)
                    else:
                        print(
                            'Failed to cancel unclaimed payout item with id: ' + item_id)
                    break

            if i == 4:
                print('Payouts batch is not processed yet')
    else:
        print('Failed to retrieve Payouts batch with id: ' + batch_id)
else:
    print('Failed to create Payouts batch')
