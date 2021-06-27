class DelegateClient(object):
    def __init__(self, nector_sdk_instance, not_allowed_controller_method_names=None):
        self.nector_sdk_instance = nector_sdk_instance

        '''
        For security purpose these methods can not be triggered from client calls
        // To whitelist calls directly from client side, remove the method name from the array
        // It is requested to call the "not_allowed_controller_method_names" only from other backend functions (idealy they should be called while performing business operations) since they cause quota consumption on nector.
        '''

        self.not_allowed_controller_method_names = ["reward_deals", "redeem_offers" "create_leads", "save_leads", "get_subscriptions", "create_taskactivities",
                                                    "create_wallets", "create_wallettransactions"] if (not_allowed_controller_method_names is None) else not_allowed_controller_method_names

    '''
    Delegate to correct method, designed to be called directly from route or controoler handler function
    Client request body structure must follow the below pattern
        req.body = {
            method: string<"name_of_method_where_to_delegate_the_call">,
            params: object<{params_of_that_method}>,
            query: object<{query_of_that_method}>
            body: object<{body_of_that_method}>
        }
    '''

    def delegate_method(self, json_data):
        if json_data is None:
            raise Exception("Something went wrong, body is required")

        method = json_data.get("method", None)
        params = json_data.get("params", {})
        query = json_data.get("query", {})
        body = json_data.get("body", {})

        if method is None or method == "delegate_method" or method in self.not_allowed_controller_method_names or getattr(self, method, None) is None:
            raise Exception("Something went wrong, please try after sometime")

        return getattr(self, method)(params, query, body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1systeminfos/get for request signature and other information
    def get_systeminfos(self, params, query, body):
        return self.nector_sdk_instance.get_coupon_service().get_infos("/systeminfos")



    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1coupons/post for request signature and other information
    def create_coupons(self, params, query, body):
        return self.nector_sdk_instance.get_coupon_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1coupons~1%7Bid%7D/get for request signature and other information
    def get_coupons(self, params, query, body):
        return self.nector_sdk_instance.get_coupon_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1coupons/get for request signature and other information
    def fetch_coupons(self, params, query, body):
        return self.nector_sdk_instance.get_coupon_service().fetch(query or {})



    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1currencies~1%7Bid%7D/get for request signature and other information
    def get_currencies(self, params, query, body):
        return self.nector_sdk_instance.get_currency_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1currencies~1%7Bid%7D/get for request signature and other information
    def get_currencies_by_currency_code(self, params, query, body):
        return self.nector_sdk_instance.get_currency_service().get_by_currency_code(query.get("currency_code"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1currencies/get for request signature and other information
    def fetch_currencies(self, params, query, body):
        return self.nector_sdk_instance.get_currency_service().fetch(query or {})



    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1dealrewards/post for request signature and other information
    def reward_deals(self, params, query, body):
        return self.nector_sdk_instance.get_deal_service().reward(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1deals~1%7Bid%7D/get for request signature and other information
    def get_deals(self, params, query, body):
        return self.nector_sdk_instance.get_deal_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1deals~1%7Bid%7D/get for request signature and other information
    def get_deals_by_sku(self, params, query, body):
        return self.nector_sdk_instance.get_deal_service().get_by_sku(query.get("sku"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1deals/get for request signature and other information
    def fetch_deals(self, params, query, body):
        return self.nector_sdk_instance.get_deal_service().fetch(query or {})


    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1offerredeems/post for request signature and other information
    def redeem_offers(self, params, query, body):
        return self.nector_sdk_instance.get_offer_service().redeem(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1offers~1%7Bid%7D/get for request signature and other information
    def get_offers(self, params, query, body):
        return self.nector_sdk_instance.get_offer_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1offers~1%7Bid%7D/get for request signature and other information
    def get_offers_by_sku(self, params, query, body):
        return self.nector_sdk_instance.get_offer_service().get_by_sku(query.get("sku"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1offers/get for request signature and other information
    def fetch_offers(self, params, query, body):
        return self.nector_sdk_instance.get_offer_service().fetch(query or {})



    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1stores~1%7Bid%7D/get for request signature and other information
    def get_stores(self, params, query, body):
        return self.nector_sdk_instance.get_store_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1stores~1%7Bid%7D/get for request signature and other information
    def get_stores_by_sku(self, params, query, body):
        return self.nector_sdk_instance.get_store_service().get_by_sku(query.get("sku"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1stores/get for request signature and other information
    def fetch_stores(self, params, query, body):
        return self.nector_sdk_instance.get_store_service().fetch(query or {})



    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1leads/post for request signature and other information
    def create_leads(self, params, query, body):
        return self.nector_sdk_instance.get_lead_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1leads~1%7Bid%7D/get for request signature and other information
    def get_leads(self, params, query, body):
        return self.nector_sdk_instance.get_lead_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1leads~1%7Bid%7D/get for request signature and other information
    def get_leads_by_email(self, params, query, body):
        return self.nector_sdk_instance.get_lead_service().get_by_email(query.get("email"), query.get("swap_id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1leads~1%7Bid%7D/get for request signature and other information
    def get_leads_by_mobile(self, params, query, body):
        return self.nector_sdk_instance.get_lead_service().get_by_mobile(query.get("mobile"), query.get("swap_id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1leads~1%7Bid%7D/get for request signature and other information
    def get_leads_by_customer_id(self, params, query, body):
        return self.nector_sdk_instance.get_lead_service().get_by_customer_id(query.get("customer_id"), query.get("swap_id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1leads~1%7Bid%7D/put for request signature and other information
    def save_leads(self, params, query, body):
        return self.nector_sdk_instance.get_lead_service().save(params.get("id"), body)




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1notifications~1%7Bid%7D/get for request signature and other information
    def get_notifications(self, params, query, body):
        return self.nector_sdk_instance.get_notification_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1notifications/get for request signature and other information
    def fetch_notifications(self, params, query, body):
        return self.nector_sdk_instance.get_notification_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1reviews/post for request signature and other information
    def create_reviews(self, params, query, body):
        return self.nector_sdk_instance.get_review_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1reviews~1%7Bid%7D/get for request signature and other information
    def get_reviews(self, params, query, body):
        return self.nector_sdk_instance.get_review_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1reviews~1%7Bid%7D/delete for request signature and other information
    def delete_reviews(self, params, query, body):
        return self.nector_sdk_instance.get_review_service().delete(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1reviews~1%7Bid%7D/put for request signature and other information
    def save_reviews(self, params, query, body):
        return self.nector_sdk_instance.get_review_service().save(params.get("id"), body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1reviews/get for request signature and other information
    def fetch_reviews(self, params, query, body):
        return self.nector_sdk_instance.get_review_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1settings~1%7Bid%7D/get for request signature and other information
    def get_subscriptions(self, params, query, body):
        return self.nector_sdk_instance.get_subscription_service().get(params.get("id"))



    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1swaps/post for request signature and other information
    def create_swaps(self, params, query, body):
        return self.nector_sdk_instance.get_swap_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1swaps~1%7Bid%7D/get for request signature and other information
    def get_swaps(self, params, query, body):
        return self.nector_sdk_instance.get_swap_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1swaps~1%7Bid%7D/get for request signature and other information
    def get_swaps_by_sku(self, params, query, body):
        return self.nector_sdk_instance.get_swap_service().get_by_sku(query.get("sku"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1swaps/get for request signature and other information
    def fetch_swaps(self, params, query, body):
        return self.nector_sdk_instance.get_swap_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1tasks~1%7Bid%7D/get for request signature and other information
    def get_tasks(self, params, query, body):
        return self.nector_sdk_instance.get_task_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1tasks~1%7Bid%7D/get for request signature and other information
    def get_tasks_by_sku(self, params, query, body):
        return self.nector_sdk_instance.get_task_service().get_by_sku(query.get("sku"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1tasks/get for request signature and other information
    def fetch_tasks(self, params, query, body):
        return self.nector_sdk_instance.get_task_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1taskactivities/post for request signature and other information
    def create_taskactivities(self, params, query, body):
        return self.nector_sdk_instance.get_taskactivity_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1taskactivities~1%7Bid%7D/get for request signature and other information
    def get_taskactivities(self, params, query, body):
        return self.nector_sdk_instance.get_taskactivity_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1taskactivities/get for request signature and other information
    def fetch_taskactivities(self, params, query, body):
        return self.nector_sdk_instance.get_taskactivity_service().fetch(query or {})


    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1surprises~1%7Bid%7D/get for request signature and other information
    def get_surprises(self, params, query, body):
        return self.nector_sdk_instance.get_surprise_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1surprises~1%7Bid%7D/get for request signature and other information
    def get_surprises_by_sku(self, params, query, body):
        return self.nector_sdk_instance.get_surprise_service().get_by_sku(query.get("sku"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1surprises/get for request signature and other information
    def fetch_surprises(self, params, query, body):
        return self.nector_sdk_instance.get_surprise_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1surpriseactivities/post for request signature and other information
    def create_surpriseactivities(self, params, query, body):
        return self.nector_sdk_instance.get_surpriseactivity_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1surpriseactivities~1%7Bid%7D/get for request signature and other information
    def get_surpriseactivities(self, params, query, body):
        return self.nector_sdk_instance.get_surpriseactivity_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1surpriseactivities/get for request signature and other information
    def fetch_surpriseactivities(self, params, query, body):
        return self.nector_sdk_instance.get_surpriseactivity_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1wallets/post for request signature and other information
    def create_wallets(self, params, query, body):
        return self.nector_sdk_instance.get_wallet_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1wallets~1%7Bid%7D/get for request signature and other information
    def get_wallets(self, params, query, body):
        return self.nector_sdk_instance.get_wallet_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1wallets/get for request signature and other information
    def fetch_wallets(self, params, query, body):
        return self.nector_sdk_instance.get_wallet_service().fetch(query or {})




    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1wallettransactions/post for request signature and other information
    def create_wallettransactions(self, params, query, body):
        return self.nector_sdk_instance.get_wallettransaction_service().create(body)

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1wallettransactions~1%7Bid%7D/get for request signature and other information
    def get_wallettransactions(self, params, query, body):
        return self.nector_sdk_instance.get_wallettransaction_service().get(params.get("id"))

    # Please refer https://apidocs.nector.io/docs/api-docs/api_reference_oas3.yaml/paths/~1wallettransactions/get for request signature and other information
    def fetch_wallettransactions(self, params, query, body):
        return self.nector_sdk_instance.get_wallettransaction_service().fetch(query or {})
