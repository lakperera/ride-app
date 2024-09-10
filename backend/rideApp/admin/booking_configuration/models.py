from django.db import models
from admin.vehicles.models import Currency  # Ensure the import is correct

class BookingSetting(models.Model):  # Update class name
    booking_setting_id = models.AutoField(primary_key=True, db_index=True)
    booking_reference_number = models.CharField(max_length=100)
    symbol = models.CharField(default=None, blank=True, max_length=10)
    Fixed_prices_priority = models.CharField(default="Zones", blank=True, max_length=100)
    Remove_decimal_zeros_from_price = models.BooleanField(default=False, blank=True)
    Enable_booking_price_breakdown = models.BooleanField(default=False, blank=True)
    Auto_delete_incomplete_bookings_after = models.BooleanField(default=False, blank=True)
    Min_booking_time = models.TimeField(default=None, blank=True)
    Enable_booking_cancellation = models.BooleanField(default=False, blank=True)
    auto_refresh = models.BooleanField(default=False, blank=True)
    refresh_time = models.TimeField(blank=True, null=True)
    time_counter = models.BooleanField(default=True)

    font_size = (
        ('1', 'small'),
        ('2', 'medium'),
        ('3', 'large'),
    )

    is_enable_meeting_board = models.BooleanField(default=True)
    name_font_size = models.CharField(max_length=1, choices=font_size)
    show_company_logo = models.CharField(max_length=1)
    show_in_contents = models.CharField(max_length=1)
    show_in_folder = models.CharField(max_length=1)

    def __str__(self):
        return f"Booking Setting {self.booking_setting_id} - {self.booking_reference_number}"
