from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO app_treemenucategory (id, name, expanded_name) 
                VALUES (1, 'main_menu', 'Main menu');

            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (1, 'Home', '', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (2, 'About company', 'about', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (3, 'Exchange rates', 'rates', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (4, 'Cross rates rub-usd', 'rates_rub-usd', 1, 3);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (5, 'Cross rates rub-usd expanded info', 'rates_rub_usd_expanded', 1, 4);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (6, 'Cross rates rub-aud', 'rates_rub-aud', 1, 3);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (7, 'Cross rates rub-aud expanded info', 'rates_rub_aud_expanded', 1, 6);
        """)
    ]
