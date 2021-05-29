import random

quant_saved_mean_Data = []
highschool_completed_data = []

for a in range(0, 1000):
    sp_quant_saved_Data = []
    sp_highschool_completed_data = []

    for i in range(0, 500):
        randomIndex_quant_saved = random.randint(0, len(quant_saved)-1)
        value_quant_saved = quant_saved[randomIndex_quant_saved]

        sp_quant_saved_Data.append(value_quant_saved)

        randomIndex_highschool_completed = random.randint(0, len(highschool_completed)-1)
        value_highschool_completed = highschool_completed[randomIndex_highschool_completed]

        sp_highschool_completed_data.append(value_highschool_completed)

    sp_quant_saved_Data_Mean = st.mean(sp_quant_saved_Data)
    quant_saved_mean_Data.append(sp_quant_saved_Data_Mean)

    sp_highschool_completed_data_mean = st.mean(sp_highschool_completed_data)
    highschool_completed_data.append(sp_highschool_completed_data_mean)


mean_quant_saved = st.mean(quant_saved_mean_Data)
median_quant_saved = st.median(quant_saved_mean_Data)
mode_quant_saved = st.mode(quant_saved_mean_Data)

highschool_completed_mean = st.mean(highschool_completed_data)
highschool_completed_median = st.median(highschool_completed_data)
highschool_completed_mode = st.mode(highschool_completed_data)

print('Sp Quant Saved Mean: ',mean_quant_saved)
print('Sp Highschool Completed Mean: ',highschool_completed_mean)