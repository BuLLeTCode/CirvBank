# CirvBank
Bank system or sort off.

# Dependenciji
- [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Git](https://git-scm.com/downloads)


# Kā palaist
- Sakonfigurējam gitu
- Atveram git shell
- Rakstam `cd kur/gribu/glabat/`
- Rakstam `git clone git@github.com:BuLLeTCode/CirvBank.git`
- Rakstam `cd CirvBank`
- Rakstam `vagrant up`
- Aizejam uzpīpēt, pagatavot kafiju, apskriet ap māju, utt. Būs ilgi.
- Kad gatavs, rakstam `vagrant ssh`
- Kad iekšā vagrantā, rakstam `cd /vagrant/CirvBank`
- Un beidzot: `python manage.py runserver 0.0.0.0:5000`
- Brauzerī links: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Admin links: [http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin)
Ja pietrūkst django pakidža, rakstam:
`vagrant provision`
vai arī var dzēst ārā visu vagranta boxu, un sakt no jauna ar `vagrant up`

# Konti
superusera konts: user: user, pw:parole123<br />
parastā usera konts: user:test, pw:parole123<br />
vēl viens parasts user: user: testUser , pw: skrien3478<br />
