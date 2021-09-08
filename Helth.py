
Check = input('Want to Check your health???Press Yes for checking & any other key for Exit')
if Check != 'Yes':
    print('You can exit')
else:

    Hel = input('Press any key for Health checkup')
    import Health
    if Hel == 1:
        Health.BP.bloodpressuresystolic()
    elif Hel == 2:
        Health.Pulse.pulsecheck()
    elif Hel == 3:
        Health.Oxy.oxygenlevel()
    else:
        Health.Temp.tempcheck()