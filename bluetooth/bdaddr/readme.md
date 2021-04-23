Changer l'adresse mac d'un dongle Bluetooth (testé avec un dongle CSR 4.0)
1. cloner le répertoire bdaddr
1. installer les dépendances  
   - <code>sudo apt install libbluetooth-dev</code>
1. compiler 
   - <code>make</code>
1. vérifier que le device voulu est bien dispo
   - <code>sudo hciconfig</code>
   - <code>sudo hciconfig hci0 up</code>
   - <code>./bdaddr</code>
1. changer l'adresse mac du device
   - <code>sudo ./bdaddr -i hci0 AC:23:3F:26:C5:33</code>
1. débrancher et rebrancher l'adaptateur
1. vérifier que l'adresse a bien changée
   - <code>sudo hciconfig</code>
  
