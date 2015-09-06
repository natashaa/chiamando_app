from .models import SOTSCallRecord


def get_round_info_dict(data_dict):
    call_status_dict = {}
    current_round = data_dict.get('current_round', 1)
    unit_id = data_dict.get('ssrecid')
    indv_record = SOTSCallRecord.objects.filter(ssrecid=unit_id)
    if not indv_record.exists():
        return call_status_dict
    old_remarks = indv_record[0].remarks if indv_record[0].remarks else ''
    new_remarks = 'Round : %s Comments: %s' % (current_round, data_dict.get('remarks'))
    if old_remarks:
        new_remarks = '%s , %s' %(old_remarks, new_remarks)
    else:
        new_remarks = old_remarks
    
    call_status_dict.update({
        'round%d_mobile1_status' % current_round: data_dict.get('round%d_mobile1_status' % current_round),
        'round%d_mobile2_status' % current_round: data_dict.get('round%d_mobile2_status' % current_round),
        'round%d_landline_status' % current_round: data_dict.get('round%d_landline_status' % current_round),
        'remarks': new_remarks
    })

    return call_status_dict
