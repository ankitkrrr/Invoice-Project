import datetime 
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from .models import Invoice, Items
from .serializers import InvoiceSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework import generics
import reportlab
from html import escape

from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io

def create(request):
    
    return render(request,'invoice/create.html')

def index(request):
    invoices = Invoice.objects.all()
    return render(request,'invoice/index.html',  {'invoices':invoices})

def render_to_pdf(template_src, context_dict):
    html = render_to_string(template_src, context_dict)
    result = io.BytesIO()



    pdf = pisa.pisaDocument(io.BytesIO (html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def print(request, pk):
    template = get_template('invoice/index.html')
    invoice = Invoice.objects.get(pk=pk)
    items = Items.objects.filter(invoice=invoice)
    total = 0
    for item in items:
        item.total = (item.quantity * item.price) + (item.quantity * item.price) * (item.tax / 100)
        total += item.total
    context = {
        'invoice': invoice,
        'items': items,
        'total': total,
        'invoice_no': f'{invoice.id:03}'
    }
    html = template.render(context)
    
    return render_to_pdf('invoice\invoice.html', context)

@api_view(['POST'])
def save_invoice(request):
    
    data = request.data
        
    seller_name=data['seller_name']
    seller_phone=data['seller_phone']
    seller_address=data['seller_address']
    buyer_name=data['buyer_name']
    buyer_phone=data['buyer_phone']
    buyer_address=data['buyer_address']
    invoice = Invoice(
        seller_name=seller_name,
        seller_phone=seller_phone,
        seller_address=seller_address,
        buyer_name=buyer_name,
        buyer_phone=buyer_phone,
        buyer_address=buyer_address,
        invoice_date=datetime.date.today()
    
    )
    invoice.save()
    items = []
    if data.get('item_name') is not None:
        
        for i in range(len(data['item_name'])):
            item_name = data['item_name'][i]
            tax = data['tax'][i]
            quantity = data['quantity'][i]
            price = data['price'][i]
            items = Items(item_name=item_name, quantity=quantity, price=price, tax=tax, invoice_id=invoice.id)
            items.save();
    id = invoice.id;
    return Response({"status": "success", "id":id})