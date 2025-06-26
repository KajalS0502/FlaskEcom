from intasend import APIService

API_PUBLISHABLE_KEY= 'ISPubKey_test_daf79d72-918e-4d80-8f01-44cc4ce77b0e'

API_TOKEN= 'ISSecretKey_test_5259a97c-7dd1-441a-9157-bc9838278076'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)

create_order = service.collect.mpesa_stk_push(phone_number=7303114464, email='test@gmail.com', amount=100, narrative='Purchase of items')

print(create_order)