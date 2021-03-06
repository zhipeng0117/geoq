# -*- coding: utf-8 -*-
# This technical data was produced for the U. S. Government under Contract No. W15P7T-13-C-F600, and
# is subject to the Rights in Technical Data-Noncommercial Items clause at DFARS 252.227-7013 (FEB 2012)

from django import forms
from geoq.core.forms import StyledModelForm
from django.forms.models import inlineformset_factory
from .models import Feature, FeatureType, Map, Layer, MapLayer

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Fieldset, ButtonHolder, Submit


class FeatureForm(StyledModelForm):
    class Meta:
        model = Feature
        excluded = ('aoi',)
        fields = ('template',)


class FeatureTypeForm(StyledModelForm):
    class Meta:
        model = FeatureType
        fields = ('name','type','category','order','properties','style',)

    def __init__(self, *args, **kwargs):
        super(FeatureTypeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(None, 'name', 'type', 'category', 'order', 'properties'),
            HTML('<hr/><p><a id="property-toggle" class="btn" data-toggle="collapse" data-target="#property-list">Edit Properties &raquo;</a></p>'),
            HTML('<div id="property-list" class="collapse">'),
            HTML('<table id="property-table" class="table"><tr><th>Property</th><th>Value</th></tr>'),
            HTML('<tr><td class="key">Type</td><td><input type="text" class="value" id="type"></td></tr>'),
            HTML('<tr><td class="key">Severity</td><td><input type="text" class="value" id="severity"></td></tr>'),
            HTML('<tr><td class="key">Name</td><td><input type="text" class="value" id="name"></td></tr>'),
            HTML('</table>'),
            HTML('<p><a id="property-ok" class="btn" >OK</a><a id="property-cancel" class="btn" style="margin-left: 50px;" >Cancel</a>'),
            HTML('<a id="property-add" class="btn" style="margin-left: 50px;" >Add Property</a></p>'),
            HTML('</div>'),
            HTML('<hr/><p></p>'),
            Fieldset(None, 'style'),
            HTML('<hr/><p><a id="style-toggle" class="btn" data-toggle="collapse" data-target="#style-list">Edit Style &raquo;</a></p>'),
            HTML('<div id="style-list" class="collapse">'),
            HTML('<table id="style-table" class="table"><tr><th>Option</th><th>Value</th></tr>'),
            HTML('<tr><td class="key">color</td><td><input type="text" class="value" id="color"></td></tr>'),
            HTML('<tr><td class="key">opacity</td><td><input type="number" min="0" max="1" step="0.1" class="value" id="opacity" placeholder="Enter a value from 0 to 1 in increments of 0.1." ></td></tr>'),
            HTML('<tr><td class="key">weight</td><td><input type="number" min="1" max="6" step="1" class="value" id="weight" placeholder="Enter a value from 1 to 6 in increments of 1."></td></tr>'),
            HTML('<tr><td class="key">fillOpacity</td><td><input type="number" class="value" id="fillOpacity"></td></tr>'),
            HTML('<tr><td class="key">iconUrl</td><td><input type="text" class="value" id="iconUrl"></td></tr>'),
            HTML('</table>'),
            HTML('<p><a id="style-ok" class="btn" >OK</a><a id="style-cancel" class="btn" style="margin-left: 50px;" >Cancel</a>'),
            HTML('<a id="style-add" class="btn" style="margin-left: 50px;" >Add Style</a></p>'),
            HTML('</div>'),
            ButtonHolder(
                HTML('<hr/><p></p>'),
                Submit('Save', 'Save', css_class='button white btn'),
            ),
        )


class MapForm(StyledModelForm):
    class Meta:
        model = Map
        fields = ('title','description','zoom','projection','center_x','center_y')

class UploadKMZForm(forms.Form):
    title = forms.CharField(max_length=50)
    kmzfile = forms.FileField()

class UploadJSONForm(forms.Form):
    title = forms.CharField(max_length=50)
    jsonfile = forms.FileField()

class LayerForm(StyledModelForm):
    class Meta:
        model = Layer
        fields = ('name','type','url','layer','attribution','description','image_format','refreshrate','transparent',
                'token','additional_domains','downloadableLink','layer_params','dynamic_params',)

    def __init__(self, *args, **kwargs):
        super(LayerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(None, 'name', 'type', 'url', 'layer', 'attribution', 'description'),
            HTML('<hr/><p><a class="btn" data-toggle="collapse" data-target="#more-options">extended form options &raquo;</a></p>'),
            Fieldset('Advanced',
                     'image_format',
                     # 'styles',
                     'refreshrate',
                     'transparent',
                     # 'enable_identify',
                     'token',
                     'additional_domains',
                     # 'constraints',
                     # 'extent',
                     # 'layer_parsing_function',
                     # 'info_format',
                     # 'root_field',
                     # 'fields_to_show',
                     'downloadableLink',
                     # 'spatial_reference',
                     'layer_params',
                     'dynamic_params',
                     css_class='collapse',
                     css_id='more-options',
                     ),
            ButtonHolder(
                HTML('<hr/><p></p>'),
                Submit('Save', 'Save', css_class='button white btn'),
            ),
        )


class MapLayerForm(StyledModelForm):
    class Meta:
        model = MapLayer
        fields = ('layer','shown','stack_order','opacity','is_base_layer','display_in_layer_switcher',)

MapInlineFormset = inlineformset_factory(Map, MapLayer, fields=('layer','shown','stack_order','opacity','is_base_layer','display_in_layer_switcher',), extra=3)
