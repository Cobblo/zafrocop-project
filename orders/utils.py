import os
from django.conf import settings


# Set GTK2 path manually (adjust path if different)
os.environ["PATH"] = "C:\Program Files\GTK2-Runtime Win64\bin" + os.environ["PATH"]

from django.template.loader import render_to_string
from weasyprint import HTML
from io import BytesIO
from django.core.mail import EmailMessage

def calculate_shipping_charge(state):
    normalized = state.strip().lower()
    print(f"DEBUG State Input: '{state}' | Normalized: '{normalized}'")
    if normalized == "tamil nadu":
        return 80
    return 120



def generate_invoice_pdf(order, payment, order_products):
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'zafrocop_logo.jpg')
    assert os.path.exists(logo_path), f"Logo file not found at: {logo_path}"
    logo_url = 'file:///' + logo_path.replace('\\', '/')

    processed_items = []
    subtotal = 0
    total_tax = 0

    for item in order_products:
        item_total = item.product_price * item.quantity
        item_tax = (item.product_price * 0.12) * item.quantity  # 12% GST on full line
        subtotal += item_total
        total_tax += item_tax

        processed_items.append({
            'product': item.product,
            'price': item.product_price,
            'quantity': item.quantity,
            'variations': item.variations.all(),
            'line_total': item_total,
            'tax': item_tax,
        })

    shipping_charge = float(order.shipping_charge or 0)  
    grand_total = subtotal + total_tax + shipping_charge


    html_string = render_to_string('invoice/invoice.html', {
        'order': order,
        'payment': payment,
        'order_products': processed_items,
        'logo_url': logo_url,
        'subtotal': subtotal,
        'tax': total_tax,
        'shipping': shipping_charge, 
        'grand_total': grand_total,  
    })

    pdf_file = BytesIO()
    HTML(string=html_string).write_pdf(pdf_file)
    pdf_file.seek(0)
    return pdf_file




def send_invoice_email(order, payment, order_products):
    subject = "Your Order Invoice - Zafrocop"
    to_email = order.email
    message = "Thank you for your order. Please find your invoice attached."

    email = EmailMessage(subject, message, to=[to_email])
    email.content_subtype = "html"

    # Generate PDF
    pdf_file = generate_invoice_pdf(order, payment, order_products)
    email.attach(f"Invoice_{order.order_number}.pdf", pdf_file.read(), 'application/pdf')
    email.send()

