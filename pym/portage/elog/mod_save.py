# elog/mod_save.py - elog dispatch module
# Copyright 2006-2007 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

import codecs
import time
from portage import os
from portage import _encodings
from portage import _unicode_encode
from portage.data import portage_uid, portage_gid
from portage.util import ensure_dirs

def process(mysettings, key, logentries, fulltext):
	path = key.replace("/", ":")

	if mysettings["PORT_LOGDIR"] != "":
		elogdir = os.path.join(mysettings["PORT_LOGDIR"], "elog")
	else:
		elogdir = os.path.join(os.sep, "var", "log", "portage", "elog")
	ensure_dirs(elogdir, uid=portage_uid, gid=portage_gid, mode=02770)

	elogfilename = elogdir+"/"+path+":"+time.strftime("%Y%m%d-%H%M%S", time.gmtime(time.time()))+".log"
	elogfile = codecs.open(_unicode_encode(elogfilename,
		encoding=_encodings['fs'], errors='strict'),
		mode='w', encoding=_encodings['content'], errors='backslashreplace')
	elogfile.write(fulltext)
	elogfile.close()

	return elogfilename
