from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

import time
volume_val=1
sessions = AudioUtilities.GetAllSessions()


while True:
    for session in sessions:
        if session.Process and session.Process.name() == 'chrome.exe':
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            
            print(volume.GetMasterVolume())
            volume.SetMasterVolume(volume_val,None)
    
    time.sleep(10)
    volume_val=volume_val - 0.2
    
    if volume_val<0:
        break
