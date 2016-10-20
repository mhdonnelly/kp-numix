# numix-icon-theme
%global commit0 e03eb71454c176a98733eafa268ff79995f8159d
# numix-icon-theme-circle
%global commit1 481bc1100f01e25e92deb7facf61436b27f9ca8a
# Numix gtk theme
%global commit2 690532bd4e45d4bc334e90467f7c354efe30840f

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name:		numix
Version:	1010
Release:	8.git%{shortcommit0}%{dist}
Summary:	Numix Project

Source0:	https://github.com/numixproject/numix-icon-theme/archive/%{commit0}.tar.gz#/numix-icon-theme-%{shortcommit0}.tar.gz
Source1:	https://github.com/numixproject/numix-icon-theme-circle/archive/%{commit1}.tar.gz#/numix-icon-theme-circle-%{shortcommit1}.tar.gz
Source2:	https://github.com/numixproject/numix-gtk-theme/archive/%{commit2}.tar.gz#/numix-gtk-theme-%{shortcommit2}.tar.gz

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

%install
cd numix-gtk-theme-%{commit2}
%{make_install}
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
%doc numix-icon-theme-circle-%{commit1}/LICENSE numix-icon-theme-circle-%{commit1}/README.md
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light

%files gtk-theme
%doc numix-gtk-theme-%{commit2}/LICENSE numix-gtk-theme-%{commit2}/README.md numix-gtk-theme-%{commit2}/CREDITS
%{_datadir}/themes/Numix

%changelog
* Thu Oct 20 2016 Ian Firns <firnsy@kororaproject.org> - 0.1.0-8
- Update to latest upstream commits

* Mon Jul 11 2016 Chris Smart <csmart@kororaproject.org> - 0.1.0-7
- Fix the spec file
- Update to latest upstream commits, adds missing GNOME icons

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
