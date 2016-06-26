# numix-icon-theme
%global commit0 101307fba4bc10793d8a5a0afe3af48e5bd195ca
# numix-icon-theme-circle
%global commit1 475d6490e3ef2fe7474493aa53d63bb40b182de5
# Numix gtk theme
%global commit2 bde0a7364864b0e3b8265c5b13969757295e1e17

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name:		numix
Version:	1010
Release:	6.git%{shortcommit0}%{dist}
Summary:	Numix Project

Source0:	https://github.com/numixproject/numix-icon-theme/archive/%{commit0}.tar.gz#/numix-icon-theme-%{shortcommit0}.tar.gz
Source1:	https://github.com/numixproject/numix-icon-theme-circle/archive/%{commit1}.tar.gz#/numix-icon-theme-circle-%{shortcommit1}.tar.gz
Source2:	https://github.com/shimmerproject/Numix/archive/%{commit2}.tar.gz#/Numix-%{shortcommit2}.tar.gz

Group:		User Interface/Desktops
License:	GPLv3
URL:		http://numixproject.org

BuildArch:	noarch

%description
Numix is the official icon theme from the Numix project.
It is heavily inspired by, and based upon parts of the Elementary, Humanity and Gnome icon themes

%package icon-theme
Group:		User Interface/Desktops
Summary:	Numix Icons
Obsoletes:	korora-icon-theme-base
Provides:	korora-icon-theme-base
%description icon-theme
Numix is the official icon theme from the Numix project. 
It is heavily inspired by, and based upon parts of the Elementary, Humanity and Gnome icon themes

%package icon-theme-circle
Group:		User Interface/Desktops
Summary:	Numix Circle Icons
Obsoletes:	korora-icon-theme
Provides:	korora-icon-theme
%description icon-theme-circle
Circle is an icon theme for Linux from the Numix project

%package gtk-theme
Group:		User Interface/Desktops
Summary:	Numix Gtk Theme
BuildRequires:	rubygem-sass gdk-pixbuf2-devel
Requires:	gtk-murrine-engine
%description gtk-theme
Numix is a modern flat theme with a combination of light and dark elements. It supports Gnome, Unity, XFCE and Openbox.

%prep
%setup -q -c %{name}-%{version}-%{release} -T -a 0
%setup -q -c %{name}-%{version}-%{release} -D -T -a 1
%setup -q -c %{name}-%{version}-%{release} -D -T -a 2

%build
cd Numix-%{commit2}
make

%install
cd Numix-%{commit2}
make install DESTDIR=%{buildroot}
cd ..

install -d %{buildroot}%{_datadir}/icons

mkdir -p %{buildroot}%{_datadir}/doc/numix-icon-theme
cp -r numix-icon-theme-%{commit0}/Numix %{buildroot}%{_datadir}/icons/Numix
cp -r numix-icon-theme-%{commit0}/Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light

mkdir -p %{buildroot}%{_datadir}/doc/numix-icon-theme-circle
cp -r numix-icon-theme-circle-%{commit1}/Numix-Circle %{buildroot}%{_datadir}/icons/Numix-Circle
cp -r numix-icon-theme-circle-%{commit1}/Numix-Circle-Light %{buildroot}%{_datadir}/icons/Numix-Circle-Light

%files icon-theme
%doc numix-icon-theme-%{commit0}/license numix-icon-theme-%{commit0}/readme.md
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light

%files icon-theme-circle
%doc numix-icon-theme-circle-%{commit1}/license numix-icon-theme-circle-%{commit1}/readme.md
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light

%files gtk-theme
%doc Numix-%{commit2}/LICENSE Numix-%{commit2}/README.md Numix-%{commit2}/CREDITS
%{_datadir}/themes/Numix

%changelog
* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-6
- adjust groups and tabstops

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-5
- fix sources setup and relative dirs

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-4
- add license and readme files

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-3
- require gdk-pixbuf2

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-2
- refactor for git use

* Sun Jan 24 2016 Sascha Spreitzer <sspreitz@redhat.com>
- Refactor to build real srpms
* Tue Nov 10 2015 Sascha Spreitzer <sspreitz@redhat.com>
- Repackaging
- Adding Shine and uTouch
