function check_password()
{

	var ps1 = eval(document.getElementById("inputPassword3")).value;
	var checkPs = eval(document.getElementById("checkPassword")).value;

	if (ps1 != checkPs)
	{
		alert("password and checkPassword are not same");
	}
}
