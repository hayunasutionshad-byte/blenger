from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def config():
    return jsonify({
        "code": 0,
        "is_server_open": true,
        "is_firewall_open": true,
        "cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "backup_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "abhotupdate_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "img_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "login_download_optionalpack": "optionalclothres:shaders|optionalpetres:optionalpetres_commonab_shader|optionallobbyres:",
        "need_track_hotupdate": true,
        "abhotupdate_check": "cache_res;assetindexer;SH-Gpp;assembly-cssharp-patch",
        "latest_release_version": "OB54",
        "min_hint_size": 1,
        "space_required_in_GB": 1.48,
        "should_check_ab_load": false,
        "force_refresh_restype": "optionalavatarres",
        "remote_version": "1.130.22",
        "server_url": "https://loginbp.ggpolarbear.com/",
        "is_review_server": false,
        "use_login_optional_download": true,
        "use_background_download": false,
        "use_background_download_lobby": false,
        "country_code": "GB",
        "client_ip": "2.25.132.119",
        "gdpr_version": 1,
        "billboard_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "billboard_msg": "",
        "web_url": "",
        "billboard_bg_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "max_store": "",
        "max_web": "",
        "max_video": "",
        "patchnote_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "multi_region": "",
        "need_check_ip_list": [],
        "network_log_server": "https://sgnetwork.ggblueshark.com/",
        "web_log_server": "https://networkselftest.ff.garena.com/api/",
        "login_failed_count": 2,
        "test_url": "",
        "core_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "core_ip_list": [
          "0.0.0.0",
          "50.109.27.134",
          "129.226.2.163",
          "129.226.1.13",
          "129.226.1.16"
        ],
        "appstore_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "backup_appstore_url": "",
        "garena_login": false,
        "garena_hint": false,
        "gop_url": "",
        "gamevar": "var_name,comment,var_type,var_value\nvar_name,comment,\"var_type float, int, bool\",var_value\nANODisabledRegions,关闭MTP的地区,string,\"IND,NA\"\nANODisabledClientVariant,ANODisabledClientVariant,string,\"ClientUsingVersion_MAX_HPE,ClientUsingVersion_FFI,ClientUsingVersion_MAX|IND,ClientUsingVersion_MAX|NA,ClientUsingVersion_NORMAL|NA\"\nEnableMtpLiteDataRegion,mtp轻特征开关,string,\"BR,EUROPE,ID,ME,US,RU,SAC,SG,TH,TW,VN,PK,ZA,BD\"\nANOEmulatorCheckDisbaledClientVariant,ANOEmulatorCheckDisbaledClientVariant,string,\"ClientUsingVersion_FFI,ClientUsingVersion_MAX,ClientUsingVersion_NORMAL\"\nForceTutorial_ChangeHudABTest,fps流程中打开hud选择界面的概率,float,-1\nEnableReportSystemTimeDelta,EnableReportSystemTimeDelta,bool,false,,",
        "remote_option_version": "optionallocres:50|optionalavatarres:791|optionalclothres:1228|optionalfootballres:27|optionalfullscreencgres:319|optionalhuntinggroundres:246|optionalinfection:125|optionalingameres:503|optionallobbyres:640|optionallonewolfres:86|optionallonewolfstrikeoutres:59|optionalludores:42|optionalmap1res:385|optionalmap2res:156|optionalmap4res:139|optionalmaphippores:118|optionalmapres:357|optionalnewblast:163|optionalpetres:910|optionalrushb:108|optionalrushingpetsres:84|optionalsnowduelres:65|optionalsocialres:223|optionaltrainingres:297|optionalugcres:844|optionalvoiceres:344|optionalwerewolves:153|optionalwerunres:92|optionalmapponyres:204|optionalugcoldparadiseres:34|optionalmultiregionres:29",
        "remote_option_version_astc": "optionallocres:50|optionalavatarres:753|optionalclothres:1228|optionalfootballres:29|optionalfullscreencgres:306|optionalhuntinggroundres:216|optionalinfection:124|optionalingameres:461|optionallobbyres:640|optionallonewolfres:206|optionallonewolfstrikeoutres:155|optionalludores:175|optionalmap1res:385|optionalmap2res:192|optionalmap4res:175|optionalmaphippores:120|optionalmapres:391|optionalnewblast:162|optionalpetres:910|optionalrushb:241|optionalrushingpetsres:217|optionalsnowduelres:65|optionalsocialres:215|optionaltrainingres:267|optionalugcres:786|optionalvoiceres:379|optionalwerewolves:286|optionalwerunres:81|optionalmapponyres:204|optionalugcoldparadiseres:33|optionalmultiregionres:27",
        "device_whitelist_version": "1.6.0",
        "whitelist_mask": 0,
        "device_whitelist_sp_version": "1.0.0",
        "whitelist_sp_mask": 0,
        "ggp_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "version": "1.130.1",
        "app_version": "1.130.1",
        "ab_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "client_ab_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "res_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/",
        "patch_cdn_url": "http://2.25.132.119:2223/cdn/live/ABHotUpdates/"
    })

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)