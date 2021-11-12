import sys
sys.path.insert(0, "..")
import socket
from opcua import Server
from time import sleep
raw = open('settings.txt', 'r').read().replace(" ", "").splitlines()
print(raw)

settings = {
    'ip':'',
    'port':0
}

for item in raw:
    name, value = item.split('=')
    try:
        settings[name] = value
    except Exception as exc:
        print(exc)
        print('Не удалось считать настройки из settings.txt')




# General_Time_Based_arr = []
# Drilling_Depth_Based_arr = []
# Drilling_Connections_arr = []
# Hydraulics_arr = []
# Trip_Time_arr = []
# Trip_Connections_arr = []
# Survey_Directional_arr
main_arr=[]

def OPCStart():
    #--------------------------------------------------------------------------------------------------------------------
    #--------------------------Server setup and config-------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:5050")
    #--------------------------------------------------------------------------------------------------------------------
    #--------------------------dataspace setup---------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------
    uri = "http://witsNodes"
    idx = server.register_namespace(uri)
    objects = server.get_objects_node()
    #--------------------------------------------------------------------------------------------------------------------
    #--------------------------Objects & variables-----------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------
    #General_Time_Based = objects.add_object(idx, "General_Time_Based")
    objNames=[
        "General_Time_Based",
        "Drilling_Depth_Based",
        "Drilling_Connections",
        "Hydraulics",
        "Trip_Time",
        "Trip_Connections",
        "Survey_Directional",
        "MWD_Formation_Evaluation",
        "MWD_Mechanical",
        "Pressure_Evaluation",
        "Mud_Tank_Volumes",
        "Chromatograph_Cycle_Based",
        "Chromatograph_Depth_Based",
        "Lagged_Mud_Properties",
        "Cuttings_Lithology",
        "Hydrocarbon_Show",
        "Cementing",
        "Drill_Stem_Testing",
        "Configuration",
        "Mud_Report",
        "Bit_Report",
        "Comments",
        "Well_Identification",
        "Vessel_Motion_Mooring_Status",
        "Weather_Sea_State"
        ]
    names = [
        ["wellIdentifier","sideTrack","recordIdentifier","sequenceIdentifier","date","time","activityCode","depthBitMeas","depthBitVert","depthHoleMeas","depthHoleVert","blockPosition","rateOfPenetrationAvg","hookLoadAvg","hookLoadMax","weightOnBitAvg","weightOnBitMax","rotaryTorqueAvg","rotaryTorqueMax","rotarySpeedAvg","standpipePressureAvg","casingChokePressure","pumpStrokeRate1","pumpStrokeRate2","pumpStrokeRate3","tankVolumeActive","tankVolumeChangeAct","mudFlowOut","mudFlowOutAvg","mudFlowInAvg","mudDensityOutAvg","mudDensityInAvg","mudTemperatureOutAvg","mudTemperatureInAvg","mudConductivityOutAvg","mudConductivityInAvg","pumpStrokeCountCum","lagStrokes","depthReturnsMeas","gasAvg"],
        ["Well_Identifier","Sidetrack_Hole_Sect_No","Record_Identifier","Sequence_Identifier","Date","Time","Activity_Code","Depth_Hole_meas","Depth_Hole_vert","Rate_of_Penetration_avg","Weight_on_Bit_surf_avg","Hookload_avg","Standpipe_Pressure_avg","Rotary_Torque_surf_avg","Rotary_Speed_surf_avg","Bit_Revolutions_cum","Mud_Density_In_avg","ECD_at_Total_Depth","Mud_Flow_In_avg","Mud_Flow_Out_avg","Mud_Flow_Out_percent","Tank_Volume_active","Cost_Distance_inst","Cost_Distance_cum","Bit_Drilled_Time","Bit_Drilled_Distance","Corr_Drilling_Exponent"],
        ["Well_Identifier","Sidetrack_Hole_Sect_No","Record_Identifier","Sequence_Identifier","Date","Time","Activity_Code","Depth_Connection_meas","Depth_Connection_vert","Depth_Hole_meas",'Depth_Hole_vert',"Elapsed_Time_Bottom_Slips","Elapsed_Time_In_Slips","Elapsed_Time_Slips_Bottom","Elapsed_Time_Pumps_Off","Running_Speed_up_max","Running_Speed_down_max","Hookload_max","String_Weight_rot_avg","Torque_Make_Up_max","Torque_Breakout_max"],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_bit_(meas)','depth_bit_(vert)','depth_hole_(meas)','depth_hole_(vert)','Mud_Density_In_(avg)','Mud_Flow_In_(avg)','Standpipe_Pressure_(avg)','Plastic_Viscosity','Yield_Point','Pressure_Loss_bit','Pressure_Loss_string','Pressure_Loss_annulus','Pressure_Loss_surface','Pressure_Loss_mud_motor','Pressure_Loss_MWD_tool','Pressure_Loss_%_at_bit','Bit_Hydraulic_Power','Bit_Hydraulic_Power_Area','Jet_Impact_Force','Jet_Velocity','Annular_Velocity_(min)','Annular_Velocity_(max)','ECD_at_Total_Depth','ECD_at_Bit','ECD_at_Casing_Shoe','Pump_Hydraulic_Power','Calc/Obs_Press.Loss_ratio','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_bit_(meas)','depth_bit_(vert)','depth_hole_(meas)','depth_hole_(vert)','trip_number','in_slips_status','hookload_(avg)','block_position','running_speed_up_(max)','running_speed_down_(max)','fill/gain_volume_obs.(cum)','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_bit_(meas)','depth_bit_(vert)','depth_hole_(meas)','depth_hole_(vert)','trip_number','connections_done','connections_remaining','elapsed_time_in_slips','elapsed_time_out_of_slips','running_speed_up_(max)','running_speed_up_(avg)','running_speed_down_(max)','running_speed_down_(avg)','hookload_(max)','hookload_(min)','hookload_(avg)','torque_make_up_(max)','torque_breakout_(max)','fill/gain_volume_obs.','fill/gain_volume_exp.','fill/gain_volume_obs.(cum)','fill/gain_volume_exp_(cum)','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_svy/reading_(meas)','depth_svy/reading_(vert)','pass_number','depth_hole_(meas)','svy_type','svy_inclination','svy_azimuth_(uncorrected)','svy_azimuth_(corrected)','svy_magnetic_toolface','svy_gravity_toolface','svy_north_south_position','svy_east_west_position','svy_dog_leg_severity','svy_rate_of_walk','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','depth_bit_(meas)','depth_bit_(vert)','pass_number','depth_resis_1_sensor_(meas)','depth_resis_1_sensor_(vert)','resis_1_reading','resis_1_(borehole_corr)','depth_resis_2_sensor_(meas)','depth_resis_2_sensor_(vert)','resis_2_reading','resis_2_(borehole_corr)','depth_g.ray_1_sensor(meas)','depth_g.ray_1_sensor(vert)','gamma_ray_1_reading','gamma_ray_1(borehole_corr)','depth_g.ray_2_sensor(meas)','depth_g.ray_2_sensor(vert)','gamma_ray_2_reading','gamma_ray_2(borehole_corr)','depth_por_1_sensor_(meas)','depth_por_1_sensor_(vert)','porosity_tool_1_reading','depth_por_2_sensor_(meas)','depth_por_2_sensor_(vert)','porosity_tool_2_reading','downhole_fluid_temp_(ann)','downhole_fluid_temp_(pipe)','downhole_fluid_resis_(ann)','downhole_fluid_resis_(pipe)','depth_form_density_(meas)','depth_form_density_(vert)','formation_density','depth_caliper_(meas)','depth_caliper_(vert)','caliper','pore_pressure_grad_mwd','frac_pressure_grad_mwd','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>','<_spare_6_>','<_spare_7_>','<_spare_8_>','<_spare_9_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','depth_bit_(meas)','depth_bit_(vert)','pass_number','bottom_hole_annulus_press','bottom_hole_internal_press','downhole_wt_on_bit_(avg)','downhole_wt_on_bit_(max)','downhole_torque_(avg)','downhole_torque_(max)','downhole_motor_rpm','mwd_tool_alternator_voltage','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>','<_spare_6_>','<_spare_7_>','<_spare_8_>','<_spare_9_>'] ,
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','depth_sample_(meas)','depth_sample_(vert)','est._form._pore_press_grad.','est._form._frac_press_grad.','est._form._overburden_grad.','est._kick_tolerance','max._permitted_sicp_(init)','connection_gas_(avg)','connection_gas_(max)','connection_gas_(last)','last_trip_gas','shale_density','cuttings_cec','cavings_%','corr._drilling_exponent','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>','<_spare_6_>','<_spare_7_>','<_spare_8_>','<_spare_9_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','tank_volume_(total)','tank_volume_(active)','tank_volume_change_(total)','tank_volume_change_(active)','tank_volume_reset_time','tank_01_volume','tank_02_volume','tank_03_volume','tank_04_volume','tank_05_volume','tank_06_volume','tank_07_volume','tank_08_volume','tank_09_volume','tank_10_volume','tank_11_volume','tank_12_volume','tank_13_volume','tank_14_volume','trip_tank_1_volume','trip_tank_2_volume','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_chrom_sample_(meas)','depth_chrom_sample_(vert)','date_chrom_sample','time_chrom_sample','methane_(c1)','ethane_(c2)','propane_(c3)','iso_butane_(ic4)','nor_butane_(nc4)','iso_pentane_(ic5)','nor_pentane_(nc5)','neo_pentane_(ec5)','iso_hexane_(ic6)','nor_hexane_(nc6)','carbon_dioxide','acetylene','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_returns_(meas)','depth_returns_(vert)','methane_(c1)_(avg)','methane_(c1)_(min)','methane_(c1)_(max)','ethane_(c2)_(avg)','ethane_(c2)_(min)','ethane_(c2)_(max)','propane_(c3)_(avg)','propane_(c3)_(min)','propane_(c3)_(max)','iso_butane_(ic4)_(avg)','iso_butane_(ic4)_(min)','iso_butane_(ic4)_(max)','nor_butane_(nc4)_(avg)','nor_butane_(nc4)_(min)','nor_butane_(nc4)_(max)','iso_pentane_(ic5)_(avg)','iso_pentane_(ic5)_(min)','iso_pentane_(ic5)_(max)','nor_pentane_(nc5)_(avg)','nor_pentane_(nc5)_(min)','nor_pentane_(nc5)_(max)','neo_pentane_(ec5)_(avg)','neo_pentane_(ec5)_(min)','neo_pentane_(ec5)_(max)','iso_hexane_(ic6)_(avg)','iso_hexane_(ic6)_(min)','iso_hexane_(ic6)_(max)','nor_hexane_(nc6)_(avg)','nor_hexane_(nc6)_(min)','nor_hexane_(nc6)_(max)','carbon_dioxide_(avg)','carbon_dioxide_(min)','carbon_dioxide_(max)','acetylene','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>',],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_returns_(meas)','depth_returns_(vert)','mud_density_in_(lagd)','mud_density_out_(avg)','mud_temperature_in_(lagd)','mud_temperature_out_(avg)','mud_conductivity_in_(lagd)','mud_conductivity_out_(avg)','hyd.sulfide_haz.pot._(avg)','hyd.sulfide_p_h_(avg)','hyd.sulfide_p_hs_(avg)','gas_in_(lagd)','gas_(avg)','gas_(max)','carbon_dioxide_(avg)','hydrogen_sulfide_(avg)','hydrogen_sulfide_(max)','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_sample_(meas)','depth_sample_(vert)','description_type','lith_1_type','lith_1_%','lith_1_classification','lith_1_color','lith_1_texture','lith_1_hardness','lith_1_grain_size','lith_1_roundness','lith_1_sorting','lith_1_matrix/cement','lith_1_accessories','lith_1_porosity','lith_1_permeability','lith_2_type','lith_2_%','lith_2_classification','lith_2_color','lith_2_texture','lith_2_hardness','lith_2_grain_size','lith_2_roundness','lith_2_sorting','lith_2_matrix/cement','lith_2_accessories','lith_2_porosity','lith_2_permeability','lith_3_type','lith_3_%','lith_3_classification','lith_4_type','lith_4_%','lith_4_classification','lith_5_type','lith_5_%','lith_5_classification','fossils','composite_show','bulk_density','cuttings_gas','calcimetry_calcite_%','calcimetry_dolomite_%','cuttings_cec','cavings_%','shale_density','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','show_number','show_intvl_top_depth_(meas)','show_intvl_top_depth_(vert)','show_intvl_bott_depth(meas)','show_intvl_bott_depth(vert)','show_lith_type','show_lith_classification','show_lith_color','show_lith_texture','show_lith_hardness','show_lith_grain_size','show_lith_roundness','show_lith_sorting','show_lith_matrix/cement','show_lith_accessories','show_lith_porosity_visible','show_lith_porosity_meas','show_lith_permeability','show_lith_stain_description','show_lith_fluor_description','show_lith_cut_description','show_lith_cuttings_gas','show_titrated_salinity','show_mud_smple_methane','show_mud_smple_ethane','show_mud_smple_propane','show_mud_smple_i_butane','show_mud_smple_n_butane','show_mud_smple_i_pentane','show_mud_smple_n_pentane','show_mud_smple_n_pentane','show_mud_smple_i_hexane','show_mud_smple_n_hexane','show_comments','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','depth_casing_shoe_(meas)','depth_casing_shoe_(vert)','cem_pump_pressure_(avg)','hookload_(avg)','block_position','cem_flow_rate_in_(calc)','cem_flow_rate_in_(avg)','cem_flow_rate_out_(avg)','cem_flow_out_%','cem_fluid_dens_in_(avg)','cem_fluid_dens_out_(avg)','ecd_at_casing_shoe','cem_fluid_temp_in_(avg)','cem_fluid_temp_out_(avg)','cem_stage_number','cem_depth_to_dv_tool','cem_fluid_type/batch','cem_cumulative_returns','cem_indiv_vol_pumped','cem_cement_vol_pumped','cem_total_vol_pumped','cem_volume_to_bump_plug','cem_no./status_of_plug(s)','cem_job_type','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','dst_identification','dst_intvl_top_depth_(meas)','dst_intvl_top_depth_(vert)','dst_intvl_bott_depth_(meas)','dst_intvl_bott_depth_(vert)','dst_tool_time','dst_state_of_well','dst_surf_pressure,_tubing','dst_surf_pressure,_casing','dst_surf_temp,_tubing','dst_bottom_hole_pressure','dst_bottom_hole_temp','dst_liquid_flow_rate','dst_gas_flow_rate','dst_total_flow_rate','dst_cum_liquid_production','dst_cum_gas_production','dst_cum_total_production','hydrogen_sulfide_(avg)','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','no._drill_string_sections','ds_section_1_od','ds_section_1_id','ds_section_1_tool_joint_id','ds_section_1_tool_joint_od','ds_section_1_mass/length','ds_section_1_length','ds_section_2_od','ds_section_2_id','ds_section_2_tool_joint_id','ds_section_2_tool_joint_od','ds_section_2_mass/length','ds_section_2_length','ds_section_3_od','ds_section_3_id','ds_section_3_tool_joint_id','ds_section_3_tool_joint_od','ds_section_3_mass/length','ds_section_3_length','ds_section_4_od','ds_section_4_id','ds_section_4_tool_joint_id','ds_section_4_tool_joint_od','ds_section_4_mass/length','ds_section_4_length','ds_section_5_od','ds_section_5_id','ds_section_5_tool_joint_id','ds_section_5_tool_joint_od','ds_section_5_mass/length','ds_section_5_length','ds_section_6_od','ds_section_6_id','ds_section_6_tool_joint_id','ds_section_6_tool_joint_od','ds_section_6_mass/length','kelly_id','kelly_length','drill_pipe_stand_length','no._joints/stand','no._hole_sections','hole_section_1_diam','hole_section_1_length','hole_section_2_diam','hole_section_2_length','hole_section_3_diam','hole_section_3_length','hole_section_4_diam','hole_section_4_length','hole_section_5_diam','pump_1_capacity','pump_1_efficiency','pump_2_capacity','pump_2_efficiency','pump_3_capacity','pump_3_efficiency','rig_operating_cost/hour','trip_rate_(dist/time)','kill_line_id','kill_line_joint_id','kill_line_joint_fraction','kill_line_length','choke_line_id','choke_line_joint_id','choke_line_joint_fraction','choke_line_length','depth_casing_shoe_(meas)','depth_casing_shoe_(vert)','depth_pit_(meas)','depth_pit_(vert)','frac_pressure_grad_at_pit','drilling_contractor','rig_name','rig_type','vendor_1_name/service','vendor_2_name/service','vendor_3_name/service','vendor_4_name/service','vendor_5_name/service','vendor_6_name/service','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','mud_rept_depth_(meas)','mud_rept_depth_(vert)','mud_rept_number','mud_rept_mud_type','mud_rept_sample_location','mud_rept_sample_date','mud_rept_sample_time','mud_rept_mud_density','mud_rept_funnel_vis','mud_rept_funnel_vis_temp','mud_rept_plastic_vis','mud_rept_yield_point','mud_rept_gel_10_sec','mud_rept_gel_10_min','mud_rept_gel_30_min','mud_rept_filtrate','mud_rept_filter_cake','mud_rept_hthp_temp','mud_rept_hthp_pressure','mud_rept_hthp_filtrate','mud_rept_hthp_filter_cake','mud_rept_solids_%_(retort)','mud_rept_water_%_(retort)','mud_rept_oil_%_(retort)','mud_rept_sand_%','mud_rept_low_grav_sol_%','mud_rept_solids_%_(calc)','mud_rept_barite_content','mud_rept_lcm_content','mud_rept_mbt_capacity','mud_rept_p_h','mud_rept_p_h_sample_temp','mud_rept_pm','mud_rept_pf','mud_rept_mf','mud_rept_p1','mud_rept_p2','mud_rept_chlorides','mud_rept_calcium','mud_rept_magnesium','mud_rept_potassium','mud_rept_rheometer_temp','mud_rept_viscom_3_rpm','mud_rept_viscom_6_rpm','mud_rept_viscom_100_rpm','mud_rept_viscom_200_rpm','mud_rept_viscom_300_rpm','mud_rept_viscom_600_rpm','mud_rept_brine_%','mud_rept_alkalinity','mud_rept_lime_content','mud_rept_elect._stability','mud_rept_ca_cl,_wt_%','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','bit_number','bit_diameter','bit_manufacturer','bit_name','bit_iadc_code','bit_serial_number','bit_cost','bit_jet_1_diameter','bit_jet_2_diameter','bit_jet_3_diameter','bit_jet_4_diameter','bit_center_jet_diameter','bit_total_flow_area','bit_starting_depth_(in)','bit_ending_depth_(out)','bit_run_drilled_distance','bit_run_drilled_time','bit_run_reamed_time','bit_penetration_rate_(avg)','bit_weight_on_bit_(avg)','bit_weight_on_bit_(max)','bit_rotary_speed_(avg)','bit_rotary_speed_(max)','bit_mud_flow_rate_(avg)','bit_mud_density_(avg)','bit_standpipe_pressure_(avg)','bit_reason_run','bit_reason_pulled','bit_grade_in','bit_grade_out','bit_shock_sub_used_?','bit_mud_motor_used_?','bit_comments','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>','<_spare_6_>','<_spare_7_>','<_spare_8_>','<_spare_9_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','depth_hole_(meas)','depth_hole_(vert)','comments'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','well_name','well_identification_number','operator','well_classification_(lahee)','well_location','well_univ.tran.mercator','well_surface_latitude','well_surface_longitude','field_name','elev_:_datum_msl','elev_:_kelly_bushing_msl','elev_:_ground_level_msl','water_depth_(mean)','spud_date','custom_field_01_identifier','custom_field_02_identifier','custom_field_03_identifier','custom_field_04_identifier','custom_field_05_identifier','custom_field_06_identifier','custom_field_07_identifier','custom_field_08_identifier','custom_field_09_identifier','custom_field_10_identifier','units_type_used','time_zone_offset','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','water_depth_(mean)','tide','vessel_heading','rig_vcg','riser_tension','rig_offset_(avg)','rig_offset_(max)','rig_offset_direction','lmrp_angle_(avg)','lmrp_angle_(max)','lmrp_angle,_direction','fluid_density_in_riser','mooring_line_#01_tens(avg)','mooring_line_#01_tens(max)','mooring_line_#02_tens(avg)','mooring_line_#02_tens(max)','mooring_line_#03_tens(avg)','mooring_line_#03_tens(max)','mooring_line_#04_tens(avg)','mooring_line_#04_tens(max)','mooring_line_#05_tens(avg)','mooring_line_#05_tens(max)','mooring_line_#06_tens(avg)','mooring_line_#06_tens(max)','mooring_line_#07_tens(avg)','mooring_line_#07_tens(max)','mooring_line_#08_tens(avg)','mooring_line_#08_tens(max)','mooring_line_#09_tens(avg)','mooring_line_#09_tens(max)','mooring_line_#10_tens(avg)','mooring_line_#10_tens(max)','mooring_line_#11_tens(avg)','mooring_line_#11_tens(max)','mooring_line_#12_tens(avg)','mooring_line_#12_tens(max)','thruster_#01,_force','thruster_#01,_direction','thruster_#02,_force','thruster_#02,_direction','thruster_#03,_force','thruster_#03,_direction','thruster_#04,_force','thruster_#04,_direction','thruster_#05,_force','thruster_#05,_direction','thruster_#06,_force','thruster_#06,_direction','thruster_#07,_force','thruster_#07,_direction','thruster_#08,_force','thruster_#08,_direction','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>'],
        ['well_identifier','sidetrack/hole_sect_no.','record_identifier','sequence_identifier','date','time','activity_code','water_depth_(mean)','air_temperature','barometric_pressure','waves,_significant_height','waves,_maximum_height','waves,_mean_period','waves,_direction','swell,_significant_height','swell,_maximum_height','swell,_mean_period','swell,_direction','wind_speed_(_1_min_)','wind_gusts_(_5_sec_)','wind_direction','anemometer_height','current_speed','current_direction','depth_current_measured','vessel_mean_draft','heave,_peak_to_peak_(sig)','heave,_peak_to_peak_(max)','heave,_mean_period','roll,_peak_to_peak_(sig)','roll,_peak_to_peak_(max)','roll,_mean_period','pitch,_peak_to_peak_(sig)','pitch,_peak_to_peak_(max)','pitch,_mean_period','yaw,_peak_to_peak_(sig)','yaw,_peak_to_peak_(max)','yaw,_mean_period','surge,_peak_to_peak_(sig)','surge,_peak_to_peak_(max)','surge,_mean_period','sway,_peak_to_peak_(sig)','sway,_peak_to_peak_(max)','sway,_mean_period','trim','heel','weather_comments','<_spare_1_>','<_spare_2_>','<_spare_3_>','<_spare_4_>','<_spare_5_>']
    ]
    cnt = 0
    for i in objNames:
        bufObj=objects.add_object(idx,i)
        bufArr=[]
        for j in names[cnt]:
            buf = bufObj.add_variable(idx, j, 0)
            bufArr.append(buf)
        main_arr.append(bufArr)
        cnt+=1
    #--------------------------------------------------------------------------------------------------------------------
    #--------------------------Server start------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------
    server.start()

def socketParser(data):
    #print('Recieved: ', data)
    print("Recieve")
    raw = str(data).replace("b'&&",'').replace('!!','').replace("'",'').split('\\r')
    for i in raw:
        clean = i.replace('\\n','')
        #print(clean)
        if clean != '' and clean!='&&' and clean != 'b0':
            try:
                buf=[]
                buf.append(clean[0:2])
                buf.append(clean[2:4])
                buf.append(clean[4:].replace(',','.'))
                if int(buf[0])-1<len(main_arr):
                    if int(buf[1])-1<len(main_arr[int(buf[0])-1]):
                        main_arr[int(buf[0])-1][int(buf[1])-1].set_value(buf[2])
            except Exception as exc:
                print(exc)
                pass
def WITSLoop():
    count = 1
    while count > 0:
        try:
            sock=socket.socket()
            sock.settimeout(5)
            print(settings['ip'],int(settings['port']))
            sock.connect((settings['ip'],int(settings['port'])))            
            print('connected')
            while True:
                data = None
                try:
                    data = sock.recv(200000)
                except socket.timeout:
                    print('timeout')
                    pass
                except Exception as exc:
                    print(exc)
                    sock.close()
                    print('closed')
                    break
                if data is None:
                    print('no data')
                    pass
                else:
                    #print('connection normal')
                    count=0;
                    try:
                        socketParser(data)
                    except Exception as exc:
                        print(exc)
                        print('cant parse')
        except Exception as exc:
            print(exc)
            print("can't establish connection")
            count += 1
            print(count)
            sleep(1)

def MainLoop():
    OPCStart()
    WITSLoop()

MainLoop()

