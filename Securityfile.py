#!/usr/bin/env python3

# ============================================================
# PROTECTED PYTHON FILE
# Original: Security.py
# Ultimate Protector V6.1
# ============================================================

import os
import sys
import subprocess
import importlib.util
import base64


PBKDF2_ITERATIONS = 600000

MAX_ATTEMPTS = 3

PASSWORD_HASH = "64fae3959119bd0aa76d071e2da5776b2a64eb14703638881321b79821829bb5"

SALT = base64.b64decode(
    "vijX0oOOvC9X/FkR/otUVD9CMggR+f93pSOxZhkLBsU="
)

ENCRYPTED_PAYLOAD = base64.b64decode(
    "Z0FBQUFBQnFzN2tGUXZ2YUJnRWMwR1Q3QUU5aGw2T3IyeUZETjJsU2NPNGp1dDBRWWJLUTZkZWxFWTVKbkNDYWJGOFFVSTBzQUJhVWZZcHN6SWF6UFlMdWNKcTJSRmVIczg5VnRSWnhhNS1qLXY1SGhEem1mRy1Ja3N5aFdHdjdOLWdzVzB1ajZHaUNUZ2xXeTZwQTg1aGhlckstVmoxalhITmc0VzE4d1d0cmxUY2pTc2ZqRDVydUg3b0V2U3NoeHRhdk9lQ2VKdGZMYk5XLUhHemc0NjQwamVjOGdPd1VlSzlBUGR5cU9EQ2VZcHpjWUhCYWFJOUJrZzhVSm1TQjZ3aW1tTnU3cnBmMi0tbEluYlFXb00zejQwNjNTbThGNjhmaGR0VEJ4ZVJYUldCQVVhY3JWYm5XYnc0NElTMEptUUF6MVdDWlRLVE5XNktGOUVlVFBLZEVwWjhUY1d2ZWdVZGNiU004aGJNeTRMRGVDVktpMFZ4bi1rQUstYnZhRldBSmJVc1pxaHlVWDBhLXZwa2ZKa0d4NWstMFU4YnNzMVJxZ3VULVZWV0h2a0xjVDlwVTFGd3VveU5RMjcybFZTMi05RGhMQkdoRGhNSVlFNnZ3SnZfWTJQODhtRFRfUEpsWUo0RXh1QktjcWFuc1I3elJJNFl6N28wVEtmaEFiNlJIMGNwcXFtUUExM3Y2LU9UWDAtLS1aXzVNcjRtZXJqQ0FNeTFoalNhMFZQSE1GUG5ubldHQmNmQTBzaDNhYmRBWFhZZDZmcU4zemxZeVdEd20yWFJKRHBUZzRxREtDXzRaLUU5YlFZUUN4RnZ6Uk1zS0kyck45Vmh5OHEweFhOYU1TNUNaQXY0OHEyTFFocmsxeEl0a1FBRlRWMW1Ya005ZHN2MERwbDNlYmdTbGN2MXF0dlZxRVBPWE9SYlNIY3ZXYm5lS20yenh6dDJ5LVNJNHhWZW00WWNWOV9nVndaVVVMOEpJcnhkcGQtTDBkVjFoemREdk92ZENzV1NLclRhV1ZCS0tfUFV6MDZDZ1lEbUZ6TjVYa2hKX3JJVnhoMmhoN3ZfQUFVNWVyOGpNOTktUWVCMWtxRWR5OTBNZGd5QWswRFZLU3BqdlFIanpiYks0N001enhaUnVKRjVLa1h5V2xBLUlfcTctVUE2LXp4eTBYR2FDeVg0Nkk3cjFYNHdtV2xMRWVaRHRpNlMxMHJKNEl1c3ZLaXJKa0Eya1hJWGhUUXFoQUNlQ0tsUExnak14N2hYLVliTXIzVzYxNlJaeFQxLVgwWC1hdThkNjZINllhX01xMmVMXzA3Ujh4dFdZamRkSmNhT3YydzZ4V0Y5NDdiZUM3UkMxU3ZVSk5MMnZEd04ySzgtZ0ZMenVVQVByZFJWREJMakE0RWktN2tRYWdlcVNpUWVXNGNqdWFHZXFMQy11bHFDejQxUkJzV3JfZUFLTUFFaFZpMTlWd0JVclBMM3o2cTV3MzhIWHI0VkpYZE9seWp5OUg5X01SWXZpXzJJbS1JMUZaaUpOZ0tTc2ItUExVRmZ5eEExVEp2TE13Ti1reU5EMW4xTEE4X0FnM3B5cG5uY1Vkd3lzVF91SGpoZm1jUmswdDVzV1VPamxHMklrTDVsZUl0M0xPMW9pYndDQVhZOGhJT0R1aDFIcXEyMnZkOE01VGdhZm8tRW0xbWVkTFF5UTBvcWo2Z3Z2OTF4cnlsOEVBaGVIMjQzZEZIeGFDbjJzcTl5T1ZwZkw5b2hZOElRbVkydG9KRFVPMHQ5dVNrMHlGWElaLVZXYmhxNWZjN010dC1JUFI4NHZta3BVZ0l1TGd6V2syWWtEaWphNnllMkc1TzJPTWhaV1RqM0N1b2FNeUo4amoyY1dkSG9fd0lJaEFQbWdfWmEtR3dvU0lNODNncjlzMnRPNXpVQ0IxUWo3dHEyNk9SbzFZNEdoVTc2RXhVQnMtaUo1cGVnVmdqMkg1UTk0ZkY2UjdtYUREZXhZMVFBZkVUamNZOEJwWTQxWGU4cmJxeE93NFhIZUEyWUxDZXkzQnhQVzNka016bW0zQjFMUmRZYzB0QU9qSTVQUzdDNmdtR3Y5aG5wZUdEU1lTbkFiQkNCSnVJSmN3MW1abXNWamwteTA1Mno2WF9hdzVFV0YzVlZnc0JXTHBNT0hhTEFkcHVfbGFYOHNiaDA1UWJ0WERCalUxcnREOHhEQ0MwTGxHdC1zVUh6U3MxdVdpMzloSndDMEYzR0hZakxZeFBUbnpfNXVTQWxDTnlCVlNBa1pFXzRLUERjcUhNWS1RMEpSSWZRNkNuX1hPLXE1NnlBX2pfVFI2QVFiUkZ6U1FkcUc0clN3TFdnaXRJaUg2cE9wZ2FaTV9vU3kyb3BLUFl3ZWNaUG1ZVHVnRWowTHVkTXhWN2ZJeVl4RF9VRndqSVo3RzR5OWczaU1Xd2FhLXlhX1JaN2t6SW5GcU42b0VPTkxKalB3TVk1NjBXVDJNMkg1VmYwTjlQNDFPOVoyQUJ1ZnBYZ2dPaWxpSzdOQjE2TGhkWExzUUdsZFJLX3BBSWtXSndremZrYlZvVkxtUXdNV1FhOFU3NXNac0d4QTZmVzRhNWVZSEdQd0hqa1c0bk02Ym51aFNvdEVGZ0ZoNGREMjVMRnh3VDUyTFRkLU1KSGZvcnBuNEJoX1A0c1U4d1ZnNlhBSlVaUHdkZVNfZ0FMallPSGYzaWtVOWM2UW5LM1QxY0hOd0ZUMHpqdm9OMlZTTW9RRjNXUWEteTNEbXpqQU5WSlMzbXR2bVJIRTYzdHkzMy11TW1FM210TFZYRkV1VEFITlNBWjNjTWlkQktiRFJSM3d6eGRtOXJBaU11bWZqaW0tUzEtWjVxNnJQT0ZTZkhReEg2ZjRtRWFZMWt4VFhhd0RLMUtkdUg1UVRGZ3BNNjNUMjlJU0VELUhDZVdaX1p5U2RMOFd2dUxhOTZ4c1RJMTBEdkUxck5EVEpvVGRTM0JCTnlSNENWZnV5cGdleWgtSkxPUjN5LUtOVUtHaFZrcWRQT01vSW54WlpTQVNiYk0wZjJ1WGthMmdSQTZtQzdxdDVra2pOMzR2MjZzNWE2S0RiWllVNng1X2RnUFRnVGZNM29XU0JUekVid0xCS0Y2SEZYRjZ5Wk90OGhYYUFXUkxwOWQ0andEdlF2T0RJc3ZIYndXcC03emtCZ0diYmQ3WXpDLUViVW5NWWxsaXNMTl9XT1JOdXI0SmIzTDVOa1JCUUtCYzJTUTNmY241UXplYXdETG1aODFmUWk5SFMtZWdUMHpuaGJ0dXk1Vm41V25qYVlrZ09YXzV0WHVBRTl0TjlfLVdaZnJ0V25tVUd0eHNSY2FralNoWTJEdnBISGNEOUxzVFFrTXVpNVJ6VGRuZ2NJaklhbGhObmhaemVlSS1jMGdaR1VPelpadWpvejJ6N2JXd0p4azZaY1ZCb213MDJEOTFyMnZFMjZQUjF6d2Q5T0N6YnlfVW9wVmFoWXJYaDhjWV9YaVY1YXJWZlpZN2xzSjJudjFOUk1ORHhwWDE4VjFHVDItSWtjMkg5S21HRlFGV2c3Ul9SbWxwczVRU2tKU2VBejc5Vmc2RWVXdnc0S1EtTzcwWGZXRko3cnhGZGtlUkVxQzJGMXJzVGpjRC1NZFZZZzV3TFYxcld4RmM4YV85TGtfQmFmTnIxMk5ucHFVaHRVWUxmcVNjR0IyLTc2NFREYjdicWRGOE0xVWFlM3B5eU8yaXZvenZYTlZVenFqVXJObm9XREFyYjNieWkxajRER096bmZRdW5PZVk2bzBwM1BfTUNiOE1PSlBPaE1xUl9SNmxzbXpmY3gyNHpnSGVETjZ5Qk5TUW5Ua24wb1gzdTFiSEppZjE3a2xmbGRBY2o2RkNZN1V4RGV0ZWxwOFQ4ZThwb3ZCbnpOM19aQXpaMGdyQXFlSTByVGNCc2R3dS0zNjh1ZlNtcjNvSlhNXy1ZNC11OVRJZWtzVTd3QUp0M3c2NjVsOWdQcjAzRmFUSTVBbnQ3MW9fQ3hSZ1FOU19jT2dKSWtQdWtPakw3bEw4UkExUEtiNmlzZEczdUV0dTZNVW5EbUp6bG5heGdnY3d1QWZoZzdod3RvNVlSSXU3aE5ZeVU0ckV3S2dsTU10QmNhWm5Dc2JIZDIwV1pSd1Q3LXdjYWM2aGM1OE1jZDg3UHBlYnhkUF9mdDhkODRlMjk5a1hITnN2QnFJSEF6N0pGblNEYzNrZWp4R1dsYTFyblQzaUc5MTFpdUw2anNQS1ZvcXppbXV3SV9ybXhmS21ZWDBQQU9LeDdiVjBqaS1LcmhYRmg0VExhX0pkaHVHSW5WNUxvVkczbnJ2Ul81eGZnVUdoeXFzVXZFclI3T1dWaHFHRU54ekE5TlZweHhTZE9RQXNLcVFQeE1kZVhjLU9CdlhZQnAxem8xekxleHBMbkRIN2RJb0ZaMzlzc0QzWmNMNGluRE1jNzN3bzlIZHAwQ2c1dXVaWDFJVDNHRExmYTFvdlh4aTdJcW9sY0FlOENzZVNzbGlVWC1Ob1FtcUFLRlF1cHZHX3hXcmV6ZkdFNHVCVVlWTGUyakxZTHZPR0xTQnowV09EbWxISHVpRm01cnRNWHR4NE9xWkU1VzhiUkNzNlk3dDlSSXlORTNIenkyUW1HUHBreHdMbzVHTE1wUXpmOVl6Tm5NeTRPR1FkV3BvenZpU25wbGR6RTY5eEl5OUFkREQzV2xWT3p0M18yZGRFeGNQeFRPUTFmbVY0UEYteXlpaG5tOHV6Z0dEQ0RpcFBqSDJfb2pQMVc4SGdPNUdkUEpmdHZWeHNuSVlJU2lDam1IVGU2LW5wS1JEZWRZZ1Azb3VpMFBBRjh0NWF4MXBHcElTdW9FSTVyMTVqblZaS3J3WmRIREZvb0N0WHZGbE1oTUd5a011ZVFoMmlWaXFlUnZMUHZ1d0NTbUhKSFJVTE1WVzY3ZThlalN4MVBKa09hNTBnWHp1VnR4Q3BlSGxBTU1rRDZ4TWI4Nk00LTRTQTNfa2hjbTdCcFZ4YkRxNW1oODZ6NHctR25kWWZyczJrOVUtUkpPRkpoU1p3ajVnSmpJUEFUODVIYTUwOER2QV8tdHAxdkktRmZlWjhsaTVGYTl6OUxFTmtaUUtkc2lmblE0QnJyQi1YV3FWT180NmF1dTVRMXNyLURRRXM1d2VOMVBRMFNVMHd3bUphTWhBS2FiZUxIeXlLZmlPUl9CWVJWX3IxclA3UmR3TVlMUUI1WE1RMmNUY0VMUVVyU0duejdPWHJvSXBTc0ZTZEN2SmUxcFhYWExVMHhwZU82d1RWZE5HZUFsemJCeUJaSFhlbDFWbm13c1poNTU3b3liWWN2cGt6QlR2YnVBM1BreHBGS2l2SjZqdzBMT3I4dmNfSVJzOUh6UmxrYlhNdEQzZ3FfOWNtaUZvZDdpLU5ob1FhWTluOUl6SjRzbGYzR1NyNm5uQlNwSXVsUW1BZjdhdXBnNnhOTVpsRy1kUUo3QlF0bEd6Tm9FeUhMV3ljM2wydDdUaTczRU1SaVRXLW5VOXhNUml3YkFxRVBhNmZjZ1VhQVd6OGlad3dGdnRMWVlrSzVfbExIVllBcTBBeGlHLTdfZ3JCNkhVeUcxYnluc2dXQ2NJXzJmNU1jVWFsbDRneTFqNU5yNnN2TEFmWHpHRzFnUjZ1eW53R2FyemMtR2c4djVYc2xRV2YtZmVTTjE4YkhDaDhvQWFwS1Z3cWNnemtobkNSRkpoY1lmWmZEOWk2V2pBaVBldUVKNUYzY0pSVkF3Rkl4clQzN3Foa1lWNkZhU2wtZC1CSWhKaURaWVE5OXFuZWVnVmNUckdCNHZaTmpHYnV0UUI1bDEzSHNTUDlPbVZHT3BXX3UxOVdFX0JKYmdYTHRKQ1hYbVRHRUxJaFVEVnN2Sk9pXzV6OXYxMEZFUjR6dV91eHRJT0w5cXFnOFZha0QzTGwyMGszVGFySGMxR1JaT3p6TFRod1VGOWFFUzBzT0tqWmtQX0liT1NTUjhvN2czRE4tZWphblV4T3hHY3Qtdmd2ZGNfall2aWJzOFEyQ2stQktkenFwelhHVThQVkNGVWRiUGp0YThUdUEteXd3R1NERWFrNHRTQmRmUU9OTmNib1FtckxyeTVKVFdSWC1yblByaEYwaWtuX3dEeFo3Rkt0VWdndmlzOVB5X0lzM3FHYmY2emxpVEpuU0NoMnpFRURyUnVRb3FtbzBJTWdBRi1nVEJuckUzRWtxX3RhUjF2YWZXUWlYaHJzSENuMUpKZnhuU1hleUNLV0xKdnd2WlRSNDQtSWlnVGFxYkx6TDVJMTRLYTJaN1ZxN181LWRGWFBhR1RmUXJWazMyaXVfTVZJODZpUUVlYWJLSnpDZmlSeWg0QTRWUURPWmZBYW0yZnlDb2IzQUxKUDZNSWdRSmJvQThxY1Y1bGoyWjFqMWQxeDF6S3JaNm53ZUZYeS1uS25oVjh2bmt5TGJCU0hNWTMyUjZka25vaGdtckVlSlVlRkY2ZHAybUxrZFBTbEhIb1RjYjhpdWlvNzhiWTAxUE00dXNGUld6TnQ4S0ZNaG1uSGFRdlJaNjFvNklfbTRlYmhxcmV0aTRYLU91T1dmQkljT1JzR3hpMXptRl9ibzRPQ3BkMVMzUEZfbThPS1ZiT19mZFVYUmo1WV85VzJELURwLTl4VldBQ1liaS1aeFJwRDJmQW5nMjYtYVVMeFhVQWpmQnZOU0NZRFp1THMyMkNkTEtnZ3I3WnRKd0pBYjNxUWVJaTVnVWVGWVBEYWFsVU9pWlRwdUhQZEpsMnpRMFJBZmRWRTEtTGM0SXNoMHhqZUw5TEFTMWw1QXJuMnU2Q1gyelVxUTNFSnFDeFJ4Vm42OVl3WFM2Rl8xUWQ3eEZVTUM5WWFHRW12dmI4TzI5d1BWYlYzM0ZFNEJUSEFJeUQ4NUFObnRCQzJBR0l5QmZrYlBWNHNrUFVmZHY2dUViQVBPOG5ERjl4UG9fdnoxaHQ4dWh5X3lZN3RRcVVzdHoxcC1keG42dDJqQlBVNm9CbGxSaEt2cGk3S2hmaFpaQUtWRkJsakNzakJmXzJoMGN1cWYwLTdsSk82WlNzdnFGb2xpbmJyY2Y1eUN2d2pfS3loV2lTZjg0SjdVOHRGdzA0Nks3TlphSXZ5MUhiWXBaeDJkeWNHNk1zeXdsVWlobjlOU2NUZVB3Q2JBcWpTYmZKSVBrTll2NFJoYmFTUzVQY1JZNHBPTXJtbkEyckxXaUxOdVhKdDNYelZMcF80ZG9pLVdJV2FRaG5HUDNPTGdGNGE1TWlVaVJ0WVJyWUhaQXF4S2VKRjY4dTVUMUVKSHYxdjMxSnNEVkRQTGcwc2FaRExrY19SaEFzSHdxS0NhQTI2aDM5aVE5allNTTlud09PbktjTjEtZ2szOWdWcGlrMzRYVTc0bnZGMC14TjR4ekx1em1seTNSaGF0UUxGdl9PT0JiUVlSUGtsM1BtZVFIYVplYWxoemVha0VTWXFGa1NKRmZYcUpSZ1BSUmxYSDZyMU40ZHJIektTOVVUZjBXNlBRU2lmUFcyTFJwUGlsQktIRDVIcnlubFRZUExXLUVtZDZKdkl1RkRsZWVsMVd5di1jRkdpTG1ib1h5a0NrVXJ4R2xCQnVPZURVd2NPNm1BTTJNSWNVU2x1eFd5Vk5MRWN3bWowZXJkV0s1eHUtTHBTYXJmNHlicmhTcjZYckZVbDdqT2pjcUYzeE5WejNKZ192b2JRT1dLMFIxWjZuRDR0Q1MydlctaHFuc3dqMmdOWUJ3dmxvN2ZfWjRWM040d0tfMU1Oay14ZWRTaDMzbHV0azI3S1B5ZkVNZzV1RF84Tk9hSzFzTDhxY0RjaHpVWjJKRXZnY0tYb013RjQxRC1jazNkSW56eHAzSkxEOTNMTmVKc1pFZXh4N0xyVXBNMDNaaGlPc1Y5LXM3dlNKZzBoYzZxd0w2OW9PTHYxQjFOaXB3WmFnQmlTQUJ3NDBlSl9WdWFObUZXb3RCUEViMXdsM2ZseDJUcEZMeGN2dmxCSzc2Smk5VVd3Z1dPa3BHRzNjNy05eUlwcURmR1R3MG10eGx2Snh3ekd2Ym50YlRUaE92MVI0TUJfc25JVVk1LUZCSGo0bTlQZGpDelJaOEI2bi1HMEdWcU9CNDN3TWQtcGo4SXI2THZsWnQwa2lDcVRoU0RaNXl6aEhXbkQtczZ0cHlpd0xHaWc5c1lUN3hwSC1tbl96NFlVLWI5OXhPUjhwTDFEMGhlZmlfUFlxdUZXQ0V0SXZyTXNvaDA1R2o5MFV1UzlnbkM2dzQyay1ETVprUGYwakJZdEJjRW1SWjl6R01BeWtmTzU0QXVMRG9HbkdRYzlVSW11YV9oYVdyWFhlNGhITDlXS1V6eDA2NWw1ZG00TWF1aFg3SFJremRFSGpLS2oyZWYzZDJtcE9OS2MwUGloWEFMczJ5RjdFWDFZT3Z0LTI5bWZEV0hKYnNTVXRtUzFPTWZDc3BlYVpVd2tjTHM3V3JTQ3ZpOGppdTQxaXBJWlRSZ0V0Q19LamhBcThYblZTV1haSHRCenpjU253ZHJBSlZKMmVGM2RLUWZTbHI2c1czTUVVaXlnR19TQUs4UVRBRFI2bF9CaFdxUXRuLUlkaFJodkk5YUFrUTFkc1JKSnhpWFVaWkZJb0JVN2lDNGthREM5cjVPOWR0elp3ZEZaZHdDUXdRYWEtYURjUXNHZW1BLUtwNlRMeFJBMC0yb1BIRlRITk1BbW4taHJseURjcEVFeDc0ZlVhb2FycDJyWEVtSHFET2t3NVRmSW00Vlh5aVgxdUpKTXkxaVN1MHM3UXhfcVhoVGF0aFY0OGFkNVRjRjlHSEVSRFh1V2c2WGpqWnh4S0NkSkRLVEFaZjVFMjFFYlpwWUluN0tBUXZVVFBpRm1zNmJSclBIQ0ktWjJvZmJG"
)


# ============================================================
# AUTO DEPENDENCY
# ============================================================

def install_crypto():

    if importlib.util.find_spec("cryptography") is not None:
        return True

    print("[+] cryptography is not installed.")
    print("[+] Attempting automatic installation...")

    try:

        termux_pkg = (
            "/data/data/com.termux/files/usr/bin/pkg"
        )

        if os.path.exists(termux_pkg):

            subprocess.run(
                [
                    "pkg",
                    "update",
                    "-y"
                ],
                check=False
            )

            subprocess.run(
                [
                    "pkg",
                    "install",
                    "-y",
                    "python",
                    "clang",
                    "rust",
                    "openssl",
                    "libffi",
                    "pkg-config"
                ],
                check=False
            )

        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--no-cache-dir",
                "cryptography"
            ],
            check=False
        )

        return (
            importlib.util.find_spec("cryptography")
            is not None
        )

    except Exception as error:

        print(
            f"Dependency installation error: {error}"
        )

        return False


if not install_crypto():

    print(
        "cryptography installation failed."
    )

    sys.exit(1)


# ============================================================
# CRYPTOGRAPHY
# ============================================================

import zlib
import hashlib

from pathlib import Path

from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.kdf.pbkdf2 import (
    PBKDF2HMAC
)


# ============================================================
# KEY
# ============================================================

def derive_key(password):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=PBKDF2_ITERATIONS
    )

    return base64.urlsafe_b64encode(
        kdf.derive(
            password.encode("utf-8")
        )
    )


# ============================================================
# PASSWORD VERIFY
# ============================================================

def verify_password(password):

    candidate = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    return candidate == PASSWORD_HASH


# ============================================================
# PASSWORD INPUT
# ============================================================

def ask_password():

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        try:

            password = input(
                "Enter protection password: "
            )

        except KeyboardInterrupt:

            print()

            return None

        if verify_password(password):

            print(
                "[+] Password correct."
            )

            return password

        attempts += 1

        remaining = MAX_ATTEMPTS - attempts

        if remaining:

            print(
                f"Wrong password! "
                f"{remaining} attempt(s) remaining."
            )

    print(
        "Too many failed attempts."
    )

    return None


# ============================================================
# DECRYPT SOURCE
# ============================================================

def decrypt_source(password):

    try:

        key = derive_key(
            password
        )

        fernet = Fernet(
            key
        )

        decrypted = fernet.decrypt(
            ENCRYPTED_PAYLOAD
        )

        source = zlib.decompress(
            decrypted
        ).decode("utf-8")

        return source

    except Exception:

        return None


# ============================================================
# EXTRACT SOURCE
# ============================================================

def extract_source():

    print()

    print("=" * 58)
    print("SOURCE EXTRACTION")
    print("=" * 58)

    password = ask_password()

    if password is None:

        print(
            "Access denied."
        )

        return 1

    source = decrypt_source(
        password
    )

    if source is None:

        print(
            "Unable to decrypt source."
        )

        return 1

    filename = input(
        "Output filename "
        "[default: extracted_source.py]: "
    ).strip()

    if not filename:

        filename = "extracted_source.py"

    output = Path(
        filename
    )

    if output.suffix.lower() != ".py":

        output = output.with_suffix(
            ".py"
        )

    try:

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                source
            )

        print()

        print(
            f"[+] Source extracted: {output}"
        )

        return 0

    except Exception as error:

        print(
            f"Error saving source: {error}"
        )

        return 1


# ============================================================
# RUN PROTECTED PROGRAM
# ============================================================

def run_protected():

    print()

    print(
        "=" * 58
    )

    print(
        "PROTECTED PROGRAM"
    )

    print(
        "=" * 58
    )

    password = ask_password()

    if password is None:

        return 1

    source = decrypt_source(
        password
    )

    if source is None:

        print(
            "Decryption failed."
        )

        return 1

    namespace = {

        "__name__": "__main__",

        "__file__": __file__,

        "__package__": None

    }

    try:

        exec(
            compile(
                source,
                "<protected>",
                "exec"
            ),
            namespace,
            namespace
        )

        return 0

    except SystemExit as error:

        try:

            return int(
                error.code or 0
            )

        except Exception:

            return 0

    except Exception as error:

        print(
            f"Protected program error: {error}"
        )

        return 1


# ============================================================
# HELP
# ============================================================

def show_help():

    print()

    print("=" * 58)

    print(
        "Protected Python File"
    )

    print("=" * 58)

    print()

    print(
        "Normal run:"
    )

    print(
        f"python {Path(__file__).name}"
    )

    print()

    print(
        "Extract source:"
    )

    print(
        f"python {Path(__file__).name} --extract"
    )

    print()

    print(
        "Show help:"
    )

    print(
        f"python {Path(__file__).name} --help"
    )


# ============================================================
# MAIN PROTECTED FILE
# ============================================================

def main():

    if len(sys.argv) > 1:

        command = sys.argv[1].lower()

        if command in (
            "--extract",
            "--get-source",
            "--show-code"
        ):

            return extract_source()

        if command in (
            "--help",
            "-h"
        ):

            show_help()

            return 0

    return run_protected()


if __name__ == "__main__":

    sys.exit(
        main()
    )

