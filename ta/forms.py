from django import forms


class ContingentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContingentForm, self).__init__(*args, **kwargs)

        for field in self.fields.itervalues():
            field.widget.attrs['class'] = 'form-control'

    emp_id = forms.IntegerField(label='Your employee id')
    reached_date = forms.DateField(label='Reached date')
    return_date = forms.DateField(label='Return date')
    rate = forms.IntegerField(label='Rate of travel')
    kms = forms.IntegerField(label='Average kms travelled daily')


class NameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)

        for field in self.fields.itervalues():
            field.widget.attrs['class'] = 'form-control'

    emp_id = forms.IntegerField(label='Your employee id')
    s_train_no = forms.CharField(label='Start train no', max_length=5)
    s_date = forms.DateField(label='Journey start date')
    s_time = forms.TimeField(label='Journey start time')
    return_train_no = forms.CharField(label='Return train no', max_length=5)
    f_date = forms.DateField(label='Journey finish date')
    f_time = forms.TimeField(label='Journey finish time')
