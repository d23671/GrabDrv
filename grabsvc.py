import _winreg
import string
h=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'System\\CurrentControlSet\\Services')
n=0
while True:
	try:
		a=_winreg.EnumKey(h,n)
		n=n+1
		k=_winreg.OpenKey(h,a)
		m=0
		grp,nam,pth,srt='','','',''
		g=0
		s=99
		while True:
			try:
				b=_winreg.EnumValue(k,m)[0]
				m=m+1
				if b.lower()=='group':
					grp=_winreg.QueryValueEx(k,'Group')[0]
				if b.lower()=='displayname':
					nam=_winreg.QueryValueEx(k,'DisplayName')[0]
				if b.lower()=='imagepath':
					pth=_winreg.QueryValueEx(k,'ImagePath')[0]
				if b.lower()=='type':
					g=_winreg.QueryValueEx(k,'Type')[0]
				if b.lower()=='start':
					srt=_winreg.QueryValueEx(k,'Start')[0]
					s=_winreg.QueryValueEx(k,'Start')[0]
			except WindowsError:
				break;
		if g==1 and s==3:
			print
			print '------------',a
			print 'Group:',grp
			print 'DisplayName:',nam
			print 'ImagePath:',pth
			print 'Start',srt
	except WindowsError:
		break