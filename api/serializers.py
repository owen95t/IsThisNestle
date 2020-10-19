from nestle.models import Brand, Parent

from rest_framework import serializers


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('PARENT_BRAND', 'BRAND_NAME', 'SHAREHOLDER', 'SUBSIDIARY', 'SUB_BRAND')

    def to_representation(self, instance):
        rep = super(BrandSerializer, self).to_representation(instance)
        rep['PARENT_BRAND'] = instance.PARENT_BRAND.PARENT_BRAND

        if instance.SHAREHOLDER:
            rep['SHAREHOLDER'] = "Yes"
        elif not instance.SHAREHOLDER:
            rep['SHAREHOLDER'] = "No"

        if instance.SUBSIDIARY:
            rep['SUBSIDIARY'] = "Yes"
        elif not instance.SUBSIDIARY:
            rep['SUBSIDIARY'] = "No"

        if instance.SUB_BRAND:
            rep['SUB_BRAND'] = "Yes"
        elif not instance.SUB_BRAND:
            rep['SUB_BRAND'] = "No"

        return rep


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('PARENT_BRAND',)
