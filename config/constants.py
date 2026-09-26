# admin-booking-controller
ADMIN_BOOKING = "/api/admin/bookings"
ADMIN_BOOKING_ID = "/api/admin/bookings/{booking_id}"
ADMIN_BOOKING_CANCLE = "/api/admin/bookings/{booking_id}/cancel"
ADMIN_BOOKING_CLOSE = "/api/admin/bookings/{booking_id}/close"
ISSUE_UPDATE = "/api/admin/bookings/{booking_id}/close"
ITEM_CANCLE = "/api/admin/bookings/{booking_id}/items/{items_id}/cancel"
ITEM_COMPLETE = "/api/admin/bookings/{booking_id}/items/{items_id}/cancel"
ITEM_RESET_OTP_ATTEMPTS = "/api/admin/bookings/{booking_id}/items/{items_id}/reset-otp-attempts"
NEAR_BY_VENDORS = "/api/admin/bookings/{booking_id}/nearby-vendors"
BOOKING_ID_NOTES = "/api/admin/bookings/{booking_id}/notes"
BOOKING_ID_PAYOUT_RELEASE = "/api/admin/bookings/{booking_id}/payout/release"
BOOKING_ID_REFUND_RECORD = "/api/admin/bookings/{booking_id}/payout/release"
BOOKING_ID_VENDOR = "/api/admin/bookings/{booking_id}/vendor"
BOOKING_ID_VENDOR_SEARCH = "/api/admin/bookings/{booking_id}/vendor-search"
BOOKING_ID_VENDOR_SEARCH_CANCLE = "/api/admin/bookings/{booking_id}/vendor-search/cancle"
BOOKING_ID_VENDOR_SEARCH_START = "/api/admin/bookings/{booking_id}/vendor-search/start"
BOOKINGS_ISSUES = "/api/admin/bookings/issues"
BOOKINGS_MATCHING = "/api/admin/bookings/matching"
BOOKINGS_OVERBOOKING = "/api/admin/bookings/overbooking"
BOOKINGS_UPCOMING = "/api/admin/bookings/upcoming"
# admin-customer-controller
ADMIN_CUSTOMERS = "/api/admin/customers"
ADMIN_CUSTOMERS_CUSTOMER_ID = "/api/admin/customers/{customerId}"
ADMIN_CUSTOMERS_CUSTOMER_ID_ACTIVATE = "/api/admin/customers/{customerId}/activate"
ADMIN_CUSTOMERS_CUSTOMER_ID_BLOCK = "/api/admin/customers/{customerId}/block"
ADMIN_CUSTOMERS_CUSTOMER_ID_COINS = "/api/admin/customers/{customerId}/coins"
ADMIN_CUSTOMERS_CUSTOMER_ID_COINS_CREDIT = "/api/admin/customers/{customerId}/coins/credit"
ADMIN_CUSTOMERS_CUSTOMER_ID_COINS_DEBIT = "/api/admin/customers/{customerId}/coins/debit"

# admin-notification-controller
ADMIN_NOTIFICATIONS = "/api/notification/send"

# admin-stats-controller
ADMIN_STATS = "/api/notification/stats"

# admin-user-controller
ADMIN_ADMINS = "/api/admin/admins"
ADMIN_ADMINS_DEACTIVATE = "/api/admin/admins/{adminId}/deactivate"
ADMIN_ADMINS_REACTIVATE = "/api/admin/admins/{adminId}/reactivate"
# app-version-controller
APP_VERSION = "/api/app-version"

# auth-controller
# booking-controller
# catalogue-admin-controller
# catalogue-controller
# customer-controller
# festive-day-admin-controller
# festive-day-controller
# payment-controller
# places-controller
# platform-config-admin-controller
# variant-admin-controller
# vendor-admin-controller
# vendor-booking-controller
# vendor-controller
VENDOR_ADDRESS="/api/vendor/address"
VENDOR_BANK_DETAILS="/api/vendor/bank-details"
VENDOR_ME="/api/vendor/me"
VENDOR_PROFILE_PICTURES="/vendor/me/profile-pic"
VENDOR_TOGGLE_ONLINE="/api/vendor/toggle-online"
# vendor-earnings-controller
VENDOR_EARNINGS = "/api/vendor/earnings"
VENDOR_EARNINGS_history = "/api/vendor/earnings/history"
# vendor-public-controller
VENDORS_NEAR_BY = "/api/vendors/nearby"
