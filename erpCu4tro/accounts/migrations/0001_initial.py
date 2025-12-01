from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def assign_permissions(apps, schema_editor):
    # Récupérer les modèles
    User = apps.get_model('auth', 'User')
    Client = apps.get_model('clients', 'Client')
    Lead = apps.get_model('leads', 'Lead')
    Claim = apps.get_model('claims', 'Claim')
    Product = apps.get_model('products', 'Product')

    # Permissions par groupe
    permissions_map = {
        'Admin': [
            ('add_user', 'auth', 'user'),
            ('change_user', 'auth', 'user'),
            ('delete_user', 'auth', 'user'),
            ('view_user', 'auth', 'user'),
            ('add_client', 'clients', 'client'),
            ('change_client', 'clients', 'client'),
            ('delete_client', 'clients', 'client'),
            ('view_client', 'clients', 'client'),
            ('add_lead', 'leads', 'lead'),
            ('change_lead', 'leads', 'lead'),
            ('delete_lead', 'leads', 'lead'),
            ('view_lead', 'leads', 'lead'),
            ('add_claim', 'claims', 'claim'),
            ('change_claim', 'claims', 'claim'),
            ('delete_claim', 'claims', 'claim'),
            ('view_claim', 'claims', 'claim'),
            ('add_product', 'products', 'product'),
            ('change_product', 'products', 'product'),
            ('delete_product', 'products', 'product'),
            ('view_product', 'products', 'product'),
        ],
        'Supervisor': [
            ('view_client', 'clients', 'client'),
            ('view_lead', 'leads', 'lead'),
            ('change_claim', 'claims', 'claim'),
            ('view_claim', 'claims', 'claim'),
            ('view_product', 'products', 'product'),
        ],
        'Operator': [
            ('view_client', 'clients', 'client'),
            ('view_lead', 'leads', 'lead'),
            ('change_claim', 'claims', 'claim'),
            ('view_claim', 'claims', 'claim'),
        ],
        'Client': [
            ('view_client', 'clients', 'client'),
            ('add_claim', 'claims', 'claim'),
            ('view_claim', 'claims', 'claim'),
        ],
    }

    for group_name, perms in permissions_map.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        group.permissions.clear()
        for codename, app_label, model_name in perms:
            try:
                content_type = ContentType.objects.get(app_label=app_label, model=model_name)
                perm = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Permission introuvable : {codename} pour {app_label}.{model_name}")

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('clients', '0001_initial'),
        ('leads', '0001_initial'),
        ('claims', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(assign_permissions),
    ]