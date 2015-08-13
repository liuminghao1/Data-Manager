function json_add(idname,new_str){
	var old_allstr = document.getElementById(idname).innerHTML;
	document.getElementById(idname).innerHTML = old_allstr + new_str;
}
function ShowMenu(TB)
{
	whichTB = document.getElementById("Menu_" + TB);
	//whichTB2 = eval("Menu_" + TB);
	if (whichTB.style.display == "none")
   	{
		//eval("Menu_" + TB + ".style.display=\"\";");
		document.getElementById("Menu_" + TB).style.display="";
		document.getElementById("left_" + TB).className="open";
   	}
   	else
   	{
		//eval("Menu_" + TB + ".style.display=\"none\";");
		document.getElementById("Menu_" + TB).style.display="none";
		document.getElementById("left_" + TB).className="close";
   	}
}
function Show_tag(c1,c2)
{
	for(i=1;i<=c2;i++)
	{
		if(i == c1)
		{
			document.getElementById("tag_" + i).style.display="";
			document.getElementById("tag_title_" + i).className="on";
		}
		else
		{
			document.getElementById("tag_" + i).style.display="none";
			document.getElementById("tag_title_" + i).className="";
		}
	}
}
function Show_ptype(c1)
{
	if(c1 == 1)
	{
		document.getElementById("ptype_on").className="disn";
		document.getElementById("ptype_off").className="";
		document.getElementById("top_ptype").className="top_ptype";
	}
	else
	{
		document.getElementById("ptype_on").className="";
		document.getElementById("ptype_off").className="disn";
		document.getElementById("top_ptype").className="top_ptype oh";	
	}
}
function BIN_loginout()
{
	if (confirm("\n纭畾閫€鍑虹鐞嗙郴缁燂紵"))
	{
		parent.location='login.php?act=logout';
	}
}

function Confirm_del(url)
{
	if (confirm('鍒犻櫎灏嗕笉鑳藉啀鎭㈠锛岀‘璁ゅ垹闄ゆ搷浣滐紵'))
	{
		top.location = url;
	}
}
function Confirm_str(str,url)
{
	if (confirm(str + '\n\n鍒犻櫎灏嗕笉鑳藉啀鎭㈠锛岀‘璁ゅ垹闄ゆ搷浣滐紵'))
	{
		top.location = url;
	}
}
function Confirm_url(str,url)
{
	if (confirm(str))
	{
		top.location = url;
	}
}

//鏃堕棿鏄剧ず鍑芥暟缇�
function Year_Month()
{  
	var now = new  Date();  
	var yy = now.getYear();  
	var mm = now.getMonth();  
	var mmm = new Array();
	mmm[0] = "January";
	mmm[1] = "February  ";
	mmm[2] = "March";
	mmm[3] = "April";
	mmm[4] = "May";
	mmm[5] = "June";
	mmm[6] = "July";
	mmm[7] = "August";
	mmm[8] = "September";
	mmm[9] = "October";
	mmm[10] = "November";
	mmm[11] = "December";
	//mm=mmm[mm];
	return(mm+1);
}
function thisYear()
{  
	var now = new Date();  
	//var yy = now.getYear();
	var yy = now.getFullYear();
	return(yy);
}
function Date_of_Today()
{  
	var now = new Date();
	return(now.getDate());
}
function CurentTime()
{  
	var now = new  Date();
	var hh = now.getHours();
	var mm = now.getMinutes();
	var ss = now.getTime() % 60000;
	ss = (ss - (ss  %  1000)) / 1000;  
	var clock = hh+':';
	if(mm < 10) clock += '0';
	clock += mm+':';
	if(ss < 10) clock += '0';
	clock  +=  ss;  
	return(clock);
}  
function refreshCalendarClock()
{
	document.getElementById('calendarClock1').innerHTML = Year_Month();
	document.getElementById('calendarClock2').innerHTML = Date_of_Today();
	document.getElementById('calendarClock3').innerHTML = thisYear();
	document.getElementById('calendarClock4').innerHTML = CurentTime();
}
