function scr_player(){
	
	#region main code
	scr_input();

	var _jump = place_meeting(x, y + v_spd, obj_collision)

	var _move = key_right - key_left  
	
	h_spd = h_spd + acc * _move;
	h_spd = clamp(h_spd, -spd, spd);
	
	//Gravidade
	v_spd = v_spd + global.grav;
	v_spd = clamp(v_spd, -v_spd_max, v_spd_max);
	
	if _move = 0{
		h_spd = lerp(h_spd, 0, dcc);
	}
	
	scr_collision();
	
	scr_player_anim();
	
	#endregion
	
	#region test 
	
	#endregion
	if _jump{
		can_jump = true;
	}
	
	if key_jump{
		states = "jump";
		v_spd = -10;
		can_jump = false;
	 }
	 
}