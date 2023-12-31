from .models import User_Card, User_Affliction, User_Allergy
from rest_framework import serializers

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Card
        #fields = ['user_id_c', 'card_nickname','user_birthday','user_gender', 'user_height', 'user_weight', 'user_affliction']
        #fields = ['card_nickname','user_birthday','user_gender', 'user_height', 'user_weight', 'user_affliction']
        fields = '__all__'
   
class USerAfflictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Affliction
        # fields = ['affliction', 'affliction_detail']    
        fields = '__all__'

class USerAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Allergy
        # fields = ['allergy',]    
        fields = '__all__'
   