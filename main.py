# This is a sample Python script.
import os
import re
import json

if __name__ == '__main__':
    print("start")


def low_first(str):
    return str[0].lower() + str[1:]


childkeys: dict[str, str] = {'gnDot3ahPortIndex': 'port', 'gnDot3ahPortErrSymbPrdWndw': 'portErrSymbPrdWndw', 'gnDot3ahPortErrSymbPrdTHR': 'portErrSymbPrdTHR', 'gnDot3ahPortErrFrmWndw': 'portErrFrmWndw', 'gnDot3ahPortErrFrmTHR': 'portErrFrmTHR', 'gnDot3ahPortErrFrmPrdWndw': 'portErrFrmPrdWndw', 'gnDot3ahPortErrFrmPrdTHR': 'portErrFrmPrdTHR', 'gnDot3ahPortErrFrmSecsSumWndw': 'portErrFrmSecsSumWndw', 'gnDot3ahPortErrFrmSecsSumTHR': 'portErrFrmSecsSumTHR', 'gnDot3ahDiscvryStatMachStatus': 'linkState', 'gnDot3ahLocalPDUStatus': 'pduStatus', 'gnDot3ahOAMVersion': 'oamVersion', 'gnDot3ahOAMRevision': 'oamRevision', 'gnDot3ahParserAction': 'parserAction', 'gnDot3ahMultiplexerAction': 'multiplexerAction', 'gnDot3ahOAMMode': 'oamMode', 'gnDot3ahUnidirectionSupport': 'unidirectionSupport', 'gnDot3ahRmtLBSupport': 'remoteLBSupport', 'gnDot3ahLinkEvents': 'linkEvents', 'gnDot3ahVariableRetrieval': 'variableRetrieval', 'gnDot3ahMaxPDUSize': 'maxPDUSize', 'gnDot3ahOUIInfo': 'ouiInfo', 'gnDot3ahVendorSpecInfo': 'vendorSpecInfo', 'gnDot3ahRmtMACAddr': 'remoteMacAddress', 'gnDot3ahRmtOAMVersion': 'oamVersion', 'gnDot3ahRmtRevision': 'oamRevision', 'gnDot3ahRmtParserAct': 'parserAction', 'gnDot3ahRmtMultiplexerAct': 'multiplexerAction', 'gnDot3ahRmtOAMMode': 'oamMode', 'gnDot3ahRmtUniDirectionalSppt': 'unidirectionSupport', 'gnDot3ahRmtLBSppt': 'remoteLBSupport', 'gnDot3ahRmtLinkEvents': 'linkEvents', 'gnDot3ahRmtVarRetrieval': 'variableRetrieval', 'gnDot3ahRmtMaxOAMPDUSize': 'maxPDUSize', 'gnDot3ahRmtOUIInfo': 'ouiInfo', 'gnDot3ahRmtVendorSpecInfo': 'vendorSpecInfo', 'gnDot3ahRmtLBEnabled': 'state', 'gnDot3ahPortUnspprtedCodesRx': 'unspprtedCodesRx', 'gnDot3ahPortUnspprtedCodesTx': 'unspprtedCodesTx', 'gnDot3ahPortInfoRx': 'infoRx', 'gnDot3ahPortInfoTx': 'infoTx', 'gnDot3ahPortUniqEvntNotificationRx': 'uniqEvntNotificationRx', 'gnDot3ahPortUniqEvntNotificationTx': 'uniqEvntNotificationTx', 'gnDot3ahPortDupliEvntNotificationRx': 'dupliEvntNotificationRx', 'gnDot3ahPortDupliEvntNotificationTx': 'dupliEvntNotificationTx', 'gnDot3ahPortLBCtrlRx': 'lbCtrlRx', 'gnDot3ahPortLBCtrlTx': 'lbCtrlTx', 'gnDot3ahPortVarReqRx': 'varReqRx', 'gnDot3ahPortVarReqTx': 'varReqTx', 'gnDot3ahPortVarRespRx': 'varRespRx', 'gnDot3ahPortVarRespTx': 'varRespTx', 'gnDot3ahPortOrgSpecRx': 'orgSpecRx', 'gnDot3ahPortOrgSpecTx': 'orgSpecTx', 'gnDot3ahLinkFaultRx': 'linkFaultRx', 'gnDot3ahLinkFaultTx': 'linkFaultTx', 'gnDot3ahDyingGaspRx': 'dyingGaspRx', 'gnDot3ahDyingGaspTx': 'dyingGaspTx', 'gnDot3ahCRIEventRx': 'criEventRx', 'gnDot3ahCRIEventTx': 'criEventTx', 'gnDot3ahSequenceNo': 'sequenceNo', 'gnDot3ahSymblPrdErrEvntTimestamp': 'symblPrdErrEvntTimestamp', 'gnDot3ahSymblPrdErrEvntWndwHi': 'symblPrdErrEvntWndwHi', 'gnDot3ahSymblPrdErrEvntTHRHi': 'symblPrdErrEvntTHRHi', 'gnDot3ahSymbPrdErrsHi': 'symbPrdErrsHi', 'gnDot3ahTotalSymbPrdErrsHi': 'totalSymbPrdErrsHi', 'gnDot3ahTotalSymbPrdErrEvnts': 'totalSymbPrdErrEvnts', 'gnDot3ahErrFrmEvntTimestamp': 'errFrmEvntTimestamp', 'gnDot3ahErrFrmEvntWndw': 'errFrmEvntWndw', 'gnDot3ahErrFrmEvntTHR': 'errFrmEvntTHR', 'gnDot3ahErrFrames': 'errFrames', 'gnDot3ahTotalErrFramesHi': 'totalErrFramesHi', 'gnDot3ahTotalErrFrmEvnts': 'totalErrFrmEvnts', 'gnDot3ahErrFrmPrdEvntTimestamp': 'errFrmPrdEvntTimestamp', 'gnDot3ahErrFrmPrdEvntWndw': 'errFrmPrdEvntWndw', 'gnDot3ahErrFrmPrdEvntTHR': 'errFrmPrdEvntTHR', 'gnDot3ahErrFrmPrdErrs': 'errFrmPrdErrs', 'gnDot3ahTotalErrFrmPrdErrsHi': 'totalErrFrmPrdErrsHi', 'gnDot3ahTotalErrFrmPrdEvnts': 'totalErrFrmPrdEvnts', 'gnDot3ahErrFrmSecsSumEvntTimstamp': 'errFrmSecsSumEvntTimstamp', 'gnDot3ahErrFrmSecsSumEvntWndw': 'errFrmSecsSumEvntWndw', 'gnDot3ahErrFrmSecsSumEvntTHR': 'errFrmSecsSumEvntTHR', 'gnDot3ahErrFrmSecsSumEvntErrs': 'errFrmSecsSumEvntErrs', 'gnDot3ahTotalErrFrmSecsSumErrs': 'totalErrFrmSecsSumErrs', 'gnDot3ahTotalErrFrmSecsSumEvnts': 'totalErrFrmSecsSumEvnts', 'gnDot3ahPeerSequenceNo': 'sequenceNo', 'gnDot3ahPeerSymblPrdErrEvntTimestamp': 'symblPrdErrEvntTimestamp', 'gnDot3ahPeerSymblPrdErrEvntWndwHi': 'symblPrdErrEvntWndwHi', 'gnDot3ahPeerSymblPrdErrEvntTHRHi': 'symblPrdErrEvntTHRHi', 'gnDot3ahPeerSymbPrdErrsHi': 'symbPrdErrsHi', 'gnDot3ahPeerTotalSymbPrdErrsHi': 'totalSymbPrdErrsHi', 'gnDot3ahPeerTotalSymbPrdErrEvnts': 'totalSymbPrdErrEvnts', 'gnDot3ahPeerErrFrmEvntTimestamp': 'errFrmEvntTimestamp', 'gnDot3ahPeerErrFrmEvntWndw': 'errFrmEvntWndw', 'gnDot3ahPeerErrFrmEvntTHR': 'errFrmEvntTHR', 'gnDot3ahPeerErrFrames': 'errFrames', 'gnDot3ahPeerTotalErrFramesHi': 'totalErrFramesHi', 'gnDot3ahPeerTotalErrFrmEvnts': 'totalErrFrmEvnts', 'gnDot3ahPeerErrFrmPrdEvntTimestamp': 'errFrmPrdEvntTimestamp', 'gnDot3ahPeerErrFrmPrdEvntWndw': 'errFrmPrdEvntWndw', 'gnDot3ahPeerErrFrmPrdEvntTHR': 'errFrmPrdEvntTHR', 'gnDot3ahPeerErrFrmPrdErrs': 'errFrmPrdErrs', 'gnDot3ahPeerTotalErrFrmPrdErrsHi': 'totalErrFrmPrdErrsHi', 'gnDot3ahPeerTotalErrFrmPrdEvnts': 'totalErrFrmPrdEvnts', 'gnDot3ahPeerErrFrmSecsSumEvntTimstamp': 'errFrmSecsSumEvntTimstamp', 'gnDot3ahPeerErrFrmSecsSumEvntWndw': 'errFrmSecsSumEvntWndw', 'gnDot3ahPeerErrFrmSecsSumEvntTHR': 'errFrmSecsSumEvntTHR', 'gnDot3ahPeerErrFrmSecsSumEvntErrs': 'errFrmSecsSumEvntErrs', 'gnDot3ahPeerTotalErrFrmSecsSumErrs': 'totalErrFrmSecsSumErrs', 'gnDot3ahPeerTotalErrFrmSecsSumEvnts': 'totalErrFrmSecsSumEvnts', 'utsMsanEthernetOamMdIndex': 'mdIndex', 'utsMsanEthernetOamMdNameFormat': 'nameFormat', 'utsMsanEthernetOamMdName': 'name', 'utsMsanEthernetOamMdLevel': 'level', 'utsMsanEthernetOamMaIndex': 'maIndex', 'utsMsanEthernetOamMaNameFormat': 'maNameFormat', 'utsMsanEthernetOamMaName': 'maName', 'utsMsanEthernetOamMaCcmInterval': 'ccmIntervalEnum', 'utsMsanEthernetOamMaVlanList': 'vlanList', 'utsMsanEthernetOamMaPrimaryVidMode': 'primaryVidMode', 'utsMsanEthernetOamMaPrimaryVid': 'primaryVid', 'utsMsanEthernetOamMepId': 'mepId', 'utsMsanEthernetOamMepMac': 'macAddress', 'utsMsanEthernetOamMepDirection': 'direction', 'utsMsanEthernetOamMepAdmin': 'adminState', 'utsMsanEthernetOamMepCcm': 'ccmOption', 'utsMsanEthernetOamMepCfmAlarmReport': 'cfmAlarmReport', 'utsMsanEthernetOamMepVlanPriority': 'vlanPriority', 'utsMsanEthernetOamMepDropPriority': 'dropPriority', 'utsMsanEthernetOamMepRdi': 'rdi', 'utsMsanEthernetOamMepRemoteMepId': 'remoteMepId', 'utsMsanEthernetOamMepRemoteMepMac': 'remoteMac', 'utsMsanEthernetOamMipId': 'mipId', 'utsMsanEthernetOamMipMac': 'macAddress', 'utsMsanEthernetOamMipAdmin': 'adminState', 'utsMsanEthernetOamMepDiagLbTargetMacType': 'destMacType', 'utsMsanEthernetOamMepDiagTargetType': 'destType', 'utsMsanEthernetOamMepDiagMpId': 'destMPId', 'utsMsanEthernetOamMepDiagMpMac': 'destMacAddress', 'utsMsanEthernetOamMepLbmCounts': 'mepLbmCounts', 'utsMsanEtherentOamMepLbTimeout': 'timeOut', 'utsMsanEthernetOamCvid': 'cVlan', 'utsMsanEthernetOamMepLoopbackResults': 'result', 'utsMsanEthernetOamMepDiagInorderLbr': 'diagInorderLbr', 'utsMsanEthernetOamMepDiagOutorderLbr': 'diagOutorderLbr', 'utsMsanEthernetOamMepDiagInvalidLbr': 'diagInvalidLbr', 'type': 'targetType', 'mpId': 'targetMpId', 'macAddress': 'targetMacAddress', 'utsMsanEthernetOamMepLtTtl': 'ttl', 'utsMsanEtherentOamMepLtrOrder': 'ltrOrder', 'utsMsanEthernetOamMepLtrTtl': 'ttl', 'utsMsanEthernetOamMepLtrFdbOnlyFlag': 'fdbOnlyFlag', 'utsMsanEthernetOamMepLtrLtmForwardFlag': 'ltmForwardFlag', 'utsMsanEthernetOamMepLtrTerminalMep': 'terminalMep', 'utsMsanEthernetOamMepLtrAction': 'ltrAction', 'utsMsanEthernetOamMepLtrIngressMac': 'ingressMac', 'utsMsanEthernetOamMepLtrEgressMac': 'egressMac', 'utsMsanEthernetOamMepLtrIngressAction': 'ingressAction', 'utsMsanEthernetOamMepLtrEgressAction': 'egressAction', 'utsMsanEthernetOamMpMacAddressNo': 'index', 'utsMsanEthernetOamMpMac': 'mac', 'utsMsanEthernetOamMpMacStatus': 'state', 'utsMsanEthernetOamMepCcmRemoteMepId': 'remoteMepId', 'utsMsanEthernetOamMepCcmRemoteMepOpState': 'remoteMepState', 'utsMsanEthernetOamMepCcmFailedOkTime': 'failedOkTime', 'utsMsanEthernetOamMepCcmRemoteMepMac': 'remoteMepMac', 'utsMsanEthernetOamMepCcmLastRdi': 'lastRdiState', 'utsIpDslamVlanInterfaceConfIfIndex': 'ifIndex', 'utsIpDslamVlanInterfaceConfSubInterfaceId': 'subInterfaceId', 'utsIpDslamVlanInterfaceConfIpAddress': 'ipAddress', 'utsIpDslamVlanInterfaceConfNetMask': 'netMask', 'utsIpDslamVlanInterfaceConfIPv6Enable': 'ipv6Enable', 'utsIpDslamVlanInterfaceConfIPv6IpAddress': 'ipv6Address', 'utsIpDslamVlanInterfaceConfIPv6PrefixLength': 'ipv6PrefixLength', 'utsIpDslamVlanInterfaceIPv6RouteIfIndex': 'ifIndex', 'utsIpDslamVlanInterfaceIPv6RouteSubInterfaceId': 'subInterfaceId', 'utsIpDslamVlanInterfaceIPv6RouteAddr': 'ipAddress', 'utsIpDslamVlanInterfaceIPv6PrefixLength': 'prefixLength', 'utsIpDslamVlanInterfaceIPv6RouteGw': 'gateway', 'genewCsmVlanDhcpRelayOption': 'dhcpRelayOption', 'genewCsmVlanPPPoERelayOption': 'pppoeRelayOption', 'genewCsmVlanDeviceIdMode': 'deviceIdMode', 'genewCsmVlanReplaceMode': 'replaceMode', 'genewCsmVlanDeviceId': 'deviceId', 'utsCsmArpEntryTimeout': 'expiryTime', 'utsIpDslamArpReTxTimeout': 'repeatTime', 'utsCsmArpEntryTotal': 'arpNum', 'utsCsmArpEntryStaticTotal': 'staticArpNum', 'utsCsmArpEntryDynamicTotal': 'dynamicArpNum', 'utsCsmArpIpInterface': 'vlan', 'utsCsmArpIpAddr': 'ipAddress', 'utsCsmArpMacAddr': 'macAddress', 'portNameFromIndexDetail': 'egressPort', 'utsCsmArpType': 'type', 'utsCsmArpAge': 'age', 'utsCsmArpProxyLayer3Vlan': 'vlan', 'utsCsmArpProxyLayer3Enable': 'enable', 'utsCsmArpProxyLayer2Vlan': 'vlan', 'utsCsmArpProxyLayer2Enable': 'enable', 'utsCsmArpProxyLayer2GatewayMac': 'macAddress', 'utsCsmArpProxyLayer2Ip': 'ipAddress', 'utsCsmArpProxyLayer2LocalProxyArpEnable': 'localProxy', 'utsCsmArpProxyLayer2RxRequest': 'rxCount', 'utsCsmArpProxyLayer2TxResponse': 'txCount', 'utsCsmDhcpGenericVlan': 'vlan', 'utsCsmDhcpGenericFunction': 'mode', 'utsCsmDhcpServerIp': 'serverAddress', 'utsCsmDhcpFilterState': 'state', 'utsCsmDhcpv6RelayStatus': 'status', 'utsCsmDhcpv6RelayRemoteIdOption': 'remoteIdOption', 'utsCsmDhcpv6RelayRemoteId': 'remoteId', 'utsCsmDhcpv6RelayClinetVlan': 'vlan', 'utsCsmDhcpv6RelayClinetRowStatus': 'status', 'utsCsmDhcpv6RelayServerVlan': 'vlan', 'utsCsmDhcpv6RelayServerIp': 'serverAddress', 'csmLoopDetectIndex': 'gnLoopDetectPortIndex', 'gnStbLoopDetectDisabled': 'gnLoopDetectDisabled', 'gnStbLoopDetectDetected': 'gnLoopDetectDetected', 'gnStbLoopDetectLoopTimes': 'gnLoopDetectLoopTimes', 'gnStbLoopDetectLastLoop': 'gnLoopDetectLastLoop', 'genewGponMulticastCtrlMode': 'mode', 'genewGponMgmtLastMembQueryIntvl': 'lastMembQueryIntvl', 'genewGponMgmtQueryInterval': 'queryInterval', 'genewGponMgmtQueryMaxRespTime': 'maxRespTime', 'genewGponMgmtRobustness': 'robustness', 'genewGponMgmtSenderIp': 'senderIp', 'genewGponMgmtSenderIpv6': 'senderIpv6', 'genewGponIgmpSnoopingVID': 'vlan', 'genewGponIgmpSnoopingGroupAddress': 'groupAddress', 'genewGponIgmpSnoopingSourceAddress': 'sourceAddress', 'genewGponIgmpSnoopingType': 'type', 'sysUpTime': 'timeSinceTopologyChange', 'igmpSnoopingList': 'egressPortList', 'genewGponIgmpSnoopingVersion': 'version', 'oltMultiGrouptoMultiVlanMapIndex': 'index', 'oltMultiGrouptoMultiVlanMapMulticastGroupAddressStart': 'addressStart', 'oltMultiGrouptoMultiVlanMapMulticastGroupAddressStop': 'addressStop', 'oltMultiGrouptoMultiVlanMapMulticastVLANID': 'vlan', 'oltMultiVlantoMultiGEMPorMapIndex': 'index', 'oltMultiVlantoMultiGEMPorMapMulticastVLANIDStart': 'vlanStart', 'oltMultiVlantoMultiGEMPorMapMulticastVLANIDStop': 'vlanStop', 'oltMultiVlantoMultiGEMPorMapMulticastGemPortNo': 'gemPort', 'utsCsmMcastFilterState': 'enable', 'oltMultiProfileIndex1': 'index1', 'oltMultiProfileIndex2': 'index2', 'oltMultiProfileGemport': 'gemPort', 'oltMultiProfileGroup': 'group', 'oltMultiProfileAuthType': 'authType', 'oltMultiProfilePreviewlength': 'previewLength', 'oltMultiProfilePreviewInterval': 'previewInterval', 'oltMultiProfilePreviewCount': 'previewCount', 'oltMultiProfilePreviewResetTime': 'previewResetTime', 'oltMultiUserViewOltId': 'slotId', 'oltMultiUserViewPortId': 'portId', 'oltMultiUserViewOnuId': 'onuId', 'oltMultiUserViewMaxNum': 'maxNum', 'oltMultiServiceSlotId': 'slotId', 'oltMultiServiceLinkId': 'portId', 'oltMultiServiceOnuId': 'onuId', 'oltMultiServiceId1': 'serviceId', 'genewGponIgmpSnoopingV6VID': 'vlan', 'genewGponIgmpSnoopingV6GroupAddress': 'groupAddress', 'genewGponIgmpSnoopingV6SourceAddress': 'sourceAddress', 'genewGponIgmpSnoopingV6Type': 'type', 'genewGponIgmpSnoopingV6Version': 'version', 'oltMultiGrouptoMultiVlanMapV6Index': 'index', 'oltMultiGrouptoMultiVlanMapV6MulticastGroupAddressStart': 'addressStart', 'oltMultiGrouptoMultiVlanMapV6MulticastGroupAddressStop': 'addressStop', 'oltMultiGrouptoMultiVlanMapV6MulticastVLANID': 'vlan', 'oltMultionuPreviewGroupid': 'groupId', 'oltMultionuPreviewSlotid': 'slotId', 'oltMultionuPreviewLinkid': 'linkId', 'oltMultionuPreviewOnuid': 'onuId', 'oltMultionuPreviewGemport': 'gemPort', 'oltMultionuPreviewLength': 'length', 'oltMultionuPreviewRepeatTime': 'leftRepeatTime', 'oltMultionuPreviewRepeatCount': 'leftRepeatCount', 'oltMultionuPreviewLeftLength': 'leftTime', 'oltMultionuPreviewResetTime': 'leftResetTime', 'utsCsmPmLoadBridgePortRx': 'portRx', 'utsCsmPmLoadBridgePortTx': 'portTx', 'utsCsmPmStatsBridgePortErrorPksRxUndersize': 'rxUndersize', 'utsCsmPmStatsBridgePortErrorPksRxFragments': 'rxFragments', 'utsCsmPmStatsBridgePortErrorPksRxJabbers': 'rxJabbers', 'utsCsmPmStatsBridgePortErrorPksRxCodeErrors': 'rxCodeErrors', 'utsCsmPmStatsBridgePortErrorPksTxDeferrals': 'txDeferrals', 'utsCsmPmStatsBridgePortErrorPksTxExcessDeferrals': 'txExcessDefrrals', 'utsCsmPmStatsBridgePortErrorPksTxSingleCollisions': 'txSingleCollisions', 'utsCsmPmStatsBridgePortErrorPksTxMultiCollisions': 'txMultiCollisions', 'utsCsmPmStatsBridgePortErrorPksTxLateCollisions': 'txLateCollisions', 'utsCommonPmStatsBridgePortErrorPksRxAlignmentError': 'rxAlignmentError', 'utsCommonPmStatsBridgePortErrorPksRxCrcError': 'rxCrcError', 'utsCommonPmStatsBridgePortErrorPksRxOversized': 'rxOversized', 'utsCommonPmStatsBridgePortRxOctets': 'txOctets', 'utsCommonPmStatsBridgePortRxPkts': 'rxPkts', 'utsCommonPmStatsBridgePortRxMcasts': 'rxMcasts', 'utsCommonPmStatsBridgePortRxBcasts': 'rxBcasts', 'utsCsmPmStatsBridgePortRxPause': 'rxPause', 'utsCsmPmStatsBridgePortRxControls': 'rxControls', 'utsCommonPmStatsBridgePortTxPkts': 'txPkts', 'utsCommonPmStatsBridgePortTxMcasts': 'txMcasts', 'utsCommonPmStatsBridgePortTxBcasts': 'txBcasts', 'utsCsmPmStatsBridgePortTxPause': 'txPause', 'utsCsmPmStatsBridgePortTxControls': 'txControls', 'utsCommonPmStatsBridgePortRxPks64Octets': 'rx64', 'utsCommonPmStatsBridgePortRxPks65to127Octets': 'rx65', 'utsCommonPmStatsBridgePortRxPks128to255ctets': 'rx128', 'utsCommonPmStatsBridgePortRxPks256to511ctets': 'rx256', 'utsCommonPmStatsBridgePortRxPks512to1023ctets': 'rx512', 'utsCommonPmStatsBridgePortRxPks1024to1518ctets': 'rx1024', 'utsCsmPmStatsBridgePortRxPks1519to1522ctets': 'rx1519', 'utsCsmPmStatsBridgePortRxJumbos': 'rxJumbos', 'utsCommonPmStatsBridgePortTxPks64Octets': 'tx64', 'utsCommonPmStatsBridgePortTxPks65to127Octets': 'tx65', 'utsCommonPmStatsBridgePortTxPks128to255ctets': 'tx128', 'utsCommonPmStatsBridgePortTxPks256to511ctets': 'tx256', 'utsCommonPmStatsBridgePortTxPks512to1023ctets': 'tx512', 'utsCommonPmStatsBridgePortTxPks1024to1518ctets': 'tx1024', 'utsCsmPmStatsBridgePortTxPks1519to1522ctets': 'tx1519', 'utsCsmPmStatsBridgePortTxJumbos': 'txJumbos', 'utsCommonPmStatsBridgePortRxDiscards': 'rxDiscards', 'utsCommonPmStatsBridgePortRxBitRate': 'rxBitRate', 'utsCommonPmStatsBridgePortTxBitRate': 'txBitRate', 'utsCommonPmStatsBridgePortRxPktsRate': 'rxPktsRate', 'utsCommonPmStatsBridgePortTxPktsRate': 'txPktsRate', 'utsCommonPmStatsBridgePort5MinRxBitRate': 'minRxBitRate', 'utsCommonPmStatsBridgePort5MinTxBitRate': 'minTxBitRate', 'utsCommonPmStatsBridgePort5MinRxPktsRate': 'minRxPktsRate', 'utsCommonPmStatsBridgePort5MinTxPktsRate': 'minTxPktsRate', 'utsCommonPmStatsBridgePort5MinPeakRxBitRate': 'minPeakRxBitRate', 'utsCommonPmStatsBridgePort5MinPeakTxBitRate': 'minPeakTxBitRate', 'utsCommonPmStatsBridgePort5MinPeakRxPktsRate': 'minPeakRxPktsRate', 'utsCommonPmStatsBridgePort5MinPeakTxPktsRate': 'minPeakTxPktsRate', 'utsIanPmGenMoCtrlAdminState': 'adminState', 'utsIanPmGenMoCtrl15MinCapacity': 'capacity15', 'utsIanPmGenMoCtrl1DayCapacity': 'capacity24', 'utsIanPmGenPerfDataCurrMoType': 'moType', 'utsIanPmGenPerfDataCurrIntervalType': 'intervalType', 'utsIanPmGenPerfDataCurrTimeElapsed': 'timeElapsed', 'utsIanPmGenPerfDataCurrValidityTag': 'validity', 'utsIanPmBridgePerfDataCurrTypicalRxOctets': 'rxOctets', 'utsIanPmBridgePerfDataCurrTypicalRxPkts': 'rxPkts', 'utsIanPmBridgePerfDataCurrTypicalRxMcasts': 'rxMcasts', 'utsIanPmBridgePerfDataCurrTypicalRxBcasts': 'txBcasts', 'utsIanPmBridgePerfDataCurrTypicalRxDiscards': 'rxDiscards', 'utsIanPmBridgePerfDataCurrTypicalTxOctets': 'txOctets', 'utsIanPmBridgePerfDataCurrTypicalTxPkts': 'txPkts', 'utsIanPmBridgePerfDataCurrTypicalTxMcasts': 'txMcasts', 'utsIanPmBridgePerfDataCurrPktLenRxPks64Octets': 'rx64', 'utsIanPmBridgePerfDataCurrPktLenRxPks65to127Octets': 'rx65', 'utsIanPmBridgePerfDataCurrPktLenRxPks128to255ctets': 'rx128', 'utsIanPmBridgePerfDataCurrPktLenRxPks256to511ctets': 'rx256', 'utsIanPmBridgePerfDataCurrPktLenRxPks512to1023ctets': 'rx512', 'utsIanPmBridgePerfDataCurrPktLenRxPks1024to1518ctets': 'rx1024', 'utsIanPmBridgePerfDataCurrPktLenTxPks64Octets': 'tx64', 'utsIanPmBridgePerfDataCurrPktLenTxPks65to127Octets': 'tx65', 'utsIanPmBridgePerfDataCurrPktLenTxPks128to255ctets': 'tx128', 'utsIanPmBridgePerfDataCurrPktLenTxPks256to511ctets': 'tx256', 'utsIanPmBridgePerfDataCurrPktLenTxPks512to1023ctets': 'tx512', 'utsIanPmBridgePerfDataCurrPktLenTxPks1024to1518ctets': 'tx1024', 'utsIanPmGenPerfDataHistMoType': 'moType', 'utsIanPmGenPerfDataHistIntervalType': 'intervalType', 'utsIanPmGenPerfDataHistIntervalNum': 'intervalNum', 'csmPMHistTime': 'timeEnd', 'utsIanPmGenPerfDataHistValidityTag': 'validity', 'utsIanPmBridgePerfDataHistTypicalRxOctets': 'rxOctets', 'utsIanPmBridgePerfDataHistTypicalRxPkts': 'rxPkts', 'utsIanPmBridgePerfDataHistTypicalRxMcasts': 'rxMcasts', 'utsIanPmBridgePerfDataHistTypicalRxBcasts': 'txBcasts', 'utsIanPmBridgePerfDataHistTypicalRxDiscards': 'rxDiscards', 'utsIanPmBridgePerfDataHistTypicalTxOctets': 'txOctets', 'utsIanPmBridgePerfDataHistTypicalTxPkts': 'txPkts', 'utsIanPmBridgePerfDataHistTypicalTxMcasts': 'txMcasts', 'utsIanPmBridgePerfDataHistPktLenRxPks64Octets': 'rx64', 'utsIanPmBridgePerfDataHistPktLenRxPks65to127Octets': 'rx65', 'utsIanPmBridgePerfDataHistPktLenRxPks128to255ctets': 'rx128', 'utsIanPmBridgePerfDataHistPktLenRxPks256to511ctets': 'rx256', 'utsIanPmBridgePerfDataHistPktLenRxPks512to1023ctets': 'rx512', 'utsIanPmBridgePerfDataHistPktLenRxPks1024to1518ctets': 'rx1024', 'utsIanPmBridgePerfDataHistPktLenTxPks64Octets': 'tx64', 'utsIanPmBridgePerfDataHistPktLenTxPks65to127Octets': 'tx65', 'utsIanPmBridgePerfDataHistPktLenTxPks128to255ctets': 'tx128', 'utsIanPmBridgePerfDataHistPktLenTxPks256to511ctets': 'tx256', 'utsIanPmBridgePerfDataHistPktLenTxPks512to1023ctets': 'tx512', 'utsIanPmBridgePerfDataHistPktLenTxPks1024to1518ctets': 'tx1024', 'utsL2SwitchQosDot1pPriority': 'priority', 'utsL2SwitchQosCosTrafficClass': 'traffic', 'utsCsmQosEgressQueueMeterQueueId': 'queueId', 'utsCsmQosEgressQueueMeterMinCir': 'minCir', 'utsCsmQosEgressQueueMeterMaxCir': 'maxCir', 'utsCsmQosEgressQueueMeterMinCbs': 'minCbs', 'utsCsmQosEgressQueueMeterMaxCbs': 'maxCbs', 'utsCsmQosDscpMapIngressDscp': 'ingressDscp', 'utsCsmQosDscpMapQueue': 'mapQueue', 'utsCsmQosDscpMapNewDscp': 'newDscp', 'utsCsmQosDscpMapDropPrecedence': 'dropPrecedence', 'utsCsmQosDropPrecedenceCtrlDeiBitEnable': 'deiBitEnable', 'utsCsmQosDropPrecedenceCtrlDropPrecedenceEnable': 'dropPrecedenceEnable', 'utsCsmQosDropPrecedenceIngressMapWithDeiSetSpri': 'priority', 'utsCsmQosDropPrecedenceIngressMapWithDeiSetDeiBit': 'deiBit', 'utsCsmQosDropPrecedenceIngressMapWithDeiSetDropPrecedence': 'dropPrecedence', 'utsCsmQosDropPrecedenceIngressMapWithDeiResetSpri': 'priority', 'utsCsmQosDropPrecedenceIngressMapWithDeiResetDropPrecedence': 'dropPrecedence', 'utsCsmQosDropPrecedenceEgressMapWithDeiSetOriginalSpri': 'originalSpri', 'utsCsmQosDropPrecedenceEgressMapWithDeiSetDropPrecedence': 'dropPrecedence', 'utsCsmQosDropPrecedenceEgressMapWithDeiSetDeibit': 'deiBit', 'utsCsmQosDropPrecedenceEgressMapWithDeiSetNewSpri': 'newSpri', 'utsCsmQosDropPrecedenceEgressMapWithDeiResetOriginalSpri': 'originalSpri', 'utsCsmQosDropPrecedenceEgressMapWithDeiResetDropPrecedence': 'dropPrecedence', 'utsCsmQosDropPrecedenceEgressMapWithDeiResetNewSpri': 'newSpri', 'ustCsmQosSchedulingPortMethod': 'method', 'ustCsmQosSchedulingQueue': 'queue', 'ustCsmQosSchedulingQueueSpEnable': 'spState', 'ustCsmQosSchedulingQueueWeight': 'weight', 'utsCsmQosRateLimitPortIngress': 'ingressRate', 'utsCsmQosRateLimitPortEgress': 'egressRate', 'utsCsmQosMeterName': 'name', 'utsCsmQosMeterType': 'type', 'utsCsmQosMeterCir': 'cir', 'utsCsmQosMeterCbs': 'cbs', 'utsCsmQosMeterPir': 'pir', 'utsCsmQosMeterPbs': 'pbs', 'utsCsmQosMeterEbs': 'ebs', 'utsCsmQosFlowActionName': 'name', 'utsCsmQosFlowActionOption': 'option', 'utsCsmQosFlowActionMeter': 'meter', 'utsCsmQosFlowActionNewSpri': 'newSpri', 'utsCsmQosFlowActionDscp': 'newDscp', 'utsCsmQosFlowActionEgressQueueSet': 'queue', 'utsCsmQosFlowActionDropPrecedenceSet': 'dropPrecedence', 'utsCsmQosFlowActionTrafficClass': 'trafficClass', 'utsCsmQosFlowActionAssignRuleIndex': 'ruleIndex', 'utsCsmQosFlowActionAssign': 'action', 'utsCsmQosDefPriorityPortPri': 'priority', 'utsCsmSecurityFloodingControlBcastThreshold': 'bcastThreshold', 'utsCsmSecurityFloodingControlMcastThreshold': 'mcastThreshold', 'utsCsmSecurityFloodingControlDlfThreshold': 'dlfThreshold', 'utsCsmSecurityFlowActionName': 'name', 'utsCsmSecurityFlowActionOption': 'option', 'utsCsmSecurityFlowActionVlanId': 'vlanId', 'utsCsmSecurityFlowActionDestMac': 'destMac', 'utsCsmSecurityFlowActionAclAction': 'aclAction', 'utsCsmSecurityFlowActionAssignRuleIndex': 'ruleIndex', 'utsCsmSecurityFlowActionAssignSecurityAction': 'action', 'utsCsmAntiMacSpoofingState': 'state', 'utsCsmAntiDosAttackState': 'state', 'utsCsmTrustDscpState': 'state', 'utsCsmIpBindIp': 'ipAddress', 'utsCsmIpBindIpMask': 'ipGateway', 'utsCsmIpBindVlan': 'vlan', 'utsCsmSecurityVlanType': 'type', 'utsCsmSecurityVlanId': 'vlanId', 'utsCsmSecurityVlanPriority': 'priority', 'utsReservedMacBehaviorMacAddr': 'macAddress', 'utsReservedMacBehaviorAction': 'action', 'utsReservedMacBehaviorIndex': 'index', 'utsCsmMsgSpeedLimitType': 'type', 'utsCsmMsgSpeedLimitRateLimit': 'rate', 'utsCsmMsgSpeedLimitCbs': 'cbs', 'gponPonProtectLinkSetId': 'setId', 'gponPonProtectType': 'setType', 'gponPonProtectSwitchOverTimeout': 'switchOverTime', 'gponPonProtectLink1SlotId': 'link1SlotId', 'gponPonProtectLink1PortId': 'link1PortId', 'gponPonProtectLink2SlotId': 'link2SlotId', 'gponPonProtectLink2PortId': 'link2PortId', 'gponPonProtectForceSwitch': 'forceSwitch', 'dot1dStpPortPriority': 'priority', 'dot1dStpPortState': 'state', 'dot1dStpPortEnable': 'adminState', 'dot1dStpPortPathCost': 'pathCost', 'dot1dStpPortDesignatedRoot': 'designatedRoot', 'dot1dStpPortDesignatedCost': 'designatedCost', 'dot1dStpPortDesignatedBridge': 'designatedBridge', 'dot1dStpPortDesignatedPort': 'designatedPort', 'utsCsmStpEnable': 'state', 'dot1dBaseBridgeAddress': 'bridgeAddress', 'dot1dStpPriority': 'priority', 'dot1dStpTopChanges': 'topoChanges', 'dot1dStpDesignatedRoot': 'designatedRoot', 'dot1dStpRootCost': 'rootCost', 'dot1dStpMaxAge': 'maxAge', 'dot1dStpHelloTime': 'helloTime', 'dot1dStpForwardDelay': 'forwardDelay', 'dot1dStpBridgeMaxAge': 'bridgeMaxAge', 'dot1dStpBridgeHelloTime': 'bridgeHelloTime', 'dot1dStpBridgeForwardDelay': 'bridgeForwardDelay', 'mstpGenBridgeMaxAge': 'bridgeMaxAge', 'mstpGenBridgeHelloTime': 'bridgeHelloTime', 'mstpGenBridgeForwardDelay': 'bridgeForwardDelay', 'mstpGenMaxAge': 'maxAge', 'mstpGenHelloTime': 'helloTime', 'mstpGenForwardDelay': 'forwardDelay', 'mstpGenMaxHops': 'maxHops', 'mstpGenHoldTime': 'holdTime', 'mstpGenMigrateTime': 'migrateTime', 'mstpGenPathCostDefault': 'pathConstDefault', 'mstpGenCapable': 'capable', 'mstpGenForceVersion': 'forceVersion', 'mstpGenCfgIdFmtSel': 'cfgIdFmtSel', 'mstpGenCfgIdName': 'cfgIdName', 'mstpGenCfgIdRevLevel': 'cfgIdRevLevel', 'mstpGenCfgIdDigest': 'cfgIdDigest', 'mstpGenReginalRoot': 'reginalRoot', 'mstpGenExternalRootCost': 'externalRootCost', 'mstpPortAdminMACEnable': 'adminState', 'mstpPortOperMACEnable': 'operationState', 'mstpPortAdminEdge': 'adminEdge', 'mstpPortOperEdge': 'operationEdge', 'mstpPortAutoEdge': 'autoEdge', 'mstpPortAdminPointToPoint': 'adminP2P', 'mstpPortOperPointToPoint': 'operationP2P', 'mstpPortHelloTime': 'helloTime', 'mstpPortAdminNonStp': 'nonStp', 'mstpPortProtocolMigration': 'protocolMigration', 'mstpMapMSTiID': 'id', 'mstpMapVlanRangeIndex': 'vlanId', 'mstpMapVlanMin': 'vlanStartId', 'mstpMapVlanMax': 'vlanEndId', 'mstpXstId': 'id', 'mstpXstBridgePriority': 'priority', 'mstpXstBridgeId': 'bridgeId', 'mstpXstDesignatedRoot': 'designatedRoot', 'mstpXstDesignatedBridge': 'designatedBridge', 'mstpXstInternalRootCost': 'internalRootCost', 'mstpXstRootPort': 'rootPort', 'mstpXstPortXstId': 'id', 'mstpXstPortState': 'portState', 'mstpXstPortRole': 'portRole', 'mstpXstPortDesignatedRoot': 'designatedRoot', 'mstpXstPortRegionalBridge': 'regionalBridge', 'mstpXstPortDesignatedBridge': 'designatedBridge', 'mstpXstPortDesignatedPort': 'designatedPort', 'mstpXstPortPriority': 'priority', 'mstpXstPortAdminInternalPathCost': 'adminInternalPathCost', 'mstpXstPortOperInternalPathCost': 'operInternalPathCost', 'dot1qVlanIndex': 'id', 'dot1qVlanStaticName': 'name', 'utsIpDslamVlanStaticExt2Mode': 'mode', 'oltCsmVlanUserIsolationEnabled': 'status', 'tagPortList': 'taggedPort', 'dot1qVlanStaticUntaggedPorts': 'untaggedPort', 'utsCsmVlanIngressFilteringEnable': 'ingressFiltering', 'utsCsmVlanIsolationEnable': 'isolationEnable', 'utsCsmVlanStpid': 'stpId', 'utsCommonBridgingFdbVlan': 'vlan', 'utsCommonBridgingFdbAddress': 'macAddress', 'utsCommonBridgingFdbType': 'type', 'utsCommonBridgingSlotId': 'slotId', 'utsCommonBridgingPortId': 'portId', 'utsCommonBridgingOnuId': 'onuId', 'utsCommonBridgingVirtualPort': 'virtualPort', 'utsCsmMacCountPerPort': 'macCount', 'utsCsmEntryTypeIndex': 'type', 'utsCsmMacCountPerType': 'statistics', 'utsCsmMacCountPerVlan': 'statistics', 'utsCommonPktClassificationMaskPriority': 'priority', 'utsCommonPktClassificationMaskName': 'name', 'utsCommonPktClassificationMaskOptions': 'option', 'utsCommonPktClassificationMaskSrcSenderIpMask': 'srcSendIp', 'iP': 'destTargetIP', 'utsCommonPktClassificationMaskSrcMacMask': 'sourceMac', 'utsCommonPktClassificationMaskDestMacMask': 'destMac', 'utsCommonPktClassificationMaskSenderMacMask': 'senderMac', 'mac': 'targetMac', 'utsCommonPktClassificationMaskSrcIpv6IpMask': 'sourceIpv6', 'utsCommonPktClassificationMaskDestIpv6IpMask': 'destIpv6', 'utsCommonPktClassificationRuleIndex': 'index', 'utsCommonPktClassificationRuleName': 'name', 'utsCommonPktClassificationRuleMaskPriority': 'maskPriority', 'utsCommonPktClassificationRuleSvid': 'svid', 'utsCommonPktClassificationRuleSpri': 'spri', 'utsCommonPktClassificationRuleCvid': 'cvid', 'utsCommonPktClassificationRuleCpri': 'cpri', 'utsCommonPktClassificationRuleEtherType': 'etherType', 'utsCommonPktClassificationRuleIpProtocolType': 'ipProtocolType', 'utsCommonPktClassificationRuleSrcMac': 'sourceMac', 'utsCommonPktClassificationRuleDestMac': 'destMac', 'utsCommonPktClassificationRuleSrcSenderIp': 'sourceSendIp', 'ip': 'destTargetIp', 'utsCommonPktClassificationRuleTosBits': 'tosBits', 'utsCommonPktClassificationRuleDscp': 'dscp', 'utsCommonPktClassificationRuleSrcTcpUdpPort': 'sourceTcpUdpPort', 'utsCommonPktClassificationRuleDestTcpUdpPort': 'destTcpUdpPort', 'utsCommonPktClassificationRuleSenderMac': 'senderMac', 'utsCommonPktClassificationRuleSrcIpv6Ip': 'sourceIpv6', 'utsCommonPktClassificationRuleDestIpv6Ip': 'destIpv6', 'utsCommonPktClassificationRuleTrafficClass': 'trafficClass', 'utsCommonPktClassificationRuleFlowLabel': 'flowLabel', 'utsCommonPktClassificationRulePonOntVp': 'rulePonOntVp', 'oltVlanTransCfgSlotNo': 'slotNo', 'oltVlanTransCfgPortNo': 'portNo', 'oltVlanTransCfgONTNo': 'onuNo', 'oltVlanTransCfgOnuVirtualPortNo': 'onuVirtualPort', 'oltVlanTransCfgSVid': 'svid', 'oltVlanTransCfgCVid': 'cvid', 'oltVlanTransCfgNewSVid': 'newSvid', 'oltVlanTransCfgNewCVid': 'newCvid', 'oltVlanTransCfgCosAct': 'cosAction', 'oltVlanTransCfgCosVal': 'cosValue', 'neVersionGX3116': 'softVersion', 'neVersionGX3600': 'softVersion', 'utsIanSnmpAccessControlIpAddress': 'ipAddress', 'utsIanSnmpAccessControlMask': 'ipMask', 'utsIanTelnetAccessControlIpAddress': 'ipAddress', 'utsIanTelnetAccessControlMask': 'ipMask', 'utsIanTftpAccessControlIpAddress': 'ipAddress', 'utsIanTftpAccessControlMask': 'ipMask', 'utsIanAlarmActiveSequenceNumber': 'sequence', 'utsIanAlarmActiveAcknowledge': 'acknowledge', 'utsIanAlarmActiveClass': 'alarmClass', 'utsIanAlarmActiveSeverity': 'alarmSeverity', 'utsAlarmInstance': 'index', 'message': 'sliceAlarmSPStr', 'utsIanAlarmEntityType': 'enType', 'utsIanAlarmActiveProbableCause': 'probableCause', 'utsIanAlarmActiveSpecificProblem': 'specificProblem', 'utsIanAlarmFilterEntityType': 'enType', 'utsIanAlarmFilterEntityInstance': 'index', 'utsIanAlarmFilterProbableCause': 'pcCode', 'utsIanAlarmFilterSpecificProblem': 'spCode', 'utsIanExternalAlarmInputIndex': 'index', 'utsIanExternalAlarmInputEnable': 'state', 'utsIanExternalAlarmInputDescription': 'description', 'utsIanExternalAlarmInputSeverity': 'severity', 'utsIanExternalAlarmInputReportCriteria': 'reportStatus', 'utsIanCurrentExternalAlarmInputStatus': 'inputStatus', 'neLabel': 'oltName', 'ipAddress': 'oltIpAddress', 'utsIanSystemInfoModuleAuxCpuUsage': 'cpuUsage', 'utsIanSystemInfoModuleAuxMemorySizeTotal': 'memoryTotal', 'utsIanSystemInfoModuleAuxMemorySizeAvailable': 'memoryAvailable', 'utsIanSystemInfoModuleAuxMemoryUsage': 'memoryUsage', 'utsIanTemperatureMgmtEnvCurrentInstant': 'currentTemp', 'neType': 'moduleName', 'shelfId': 'boardIndex', 'utsIanFileModuleVersionCheckRequired': 'vendorVersion', 'utsIanFileModuleVersionCheckRunning': 'actualVersion', 'versionCheckResult': 'result', 'utsIanGeOpticalTempHighAlarm': 'tempHighAlarm', 'utsIanGeOpticalTempLowAlarm': 'tempLowAlarm', 'utsIanGeOpticalTempHighWarning': 'tempHighWarning', 'utsIanGeOpticalTempLowWarning': 'tempLowWarning', 'utsIanGeOpticalVoltageHighAlarm': 'voltageHighAlarm', 'utsIanGeOpticalVoltageLowAlarm': 'voltageLowAlarm', 'utsIanGeOpticalVoltageHighWarning': 'voltageHighWarning', 'utsIanGeOpticalVoltageLowWarning': 'voltageLowWarning', 'utsIanGeOpticalCurrentHighAlarm': 'currentHighAlarm', 'utsIanGeOpticalCurrentLowAlarm': 'currentLowAlarm', 'utsIanGeOpticalCurrentHighWarning': 'currentHighWarning', 'utsIanGeOpticalCurrentLowWarning': 'currentLowWarning', 'utsIanGeOpticalTxPowerHighAlarm': 'txPowerHighAlarm', 'utsIanGeOpticalTxPowerLowAlarm': 'txPowerLowAlarm', 'utsIanGeOpticalTxPowerHighWarning': 'txPowerHighWarning', 'utsIanGeOpticalTxPowerLowWarning': 'txPowerLowWarning', 'utsIanGeOpticalRxPowerHighAlarm': 'rxPowerHighAlarm', 'utsIanGeOpticalRxPowerLowAlarm': 'rxPowerLowAlarm', 'utsIanGeOpticalRxPowerHighWarning': 'rxPowerHighWarning', 'utsIanGeOpticalRxPowerLowWarning': 'rxPowerLowWarning', 'ianModuleEntityIndex': 'index', 'utsIanGeOpticalTransceiverTemp': 'temperature', 'utsIanGeOpticalTransceiverVoltage': 'voltage', 'utsIanGeOpticalTransceiverCurrent': 'current', 'utsIanGeOpticalTransceiverTxPower': 'txPower', 'utsIanGeOpticalTransceiverRxPower': 'rxPower', 'gnEnergySavingPortSwitchSlotid': 'gnEnergySavingBoardSwitchSlotid', 'gnEnergySavingPortSwitchMode': 'gnEnergySavingBoardSwitchMode', 'gnEnergySavingPortSwitchManual': 'gnEnergySavingBoardSwitchManual', 'gnEnergySavingPortSwitchStatus': 'gnEnergySavingBoardSwitchStatus', 'onuCfgPortNo': 'portNo', 'onuCfgLogicalPortNo': 'onuId', 'onuCfgOperationalState': 'operationState', 'onuCfgPrimaryStatus': 'primaryStatus', 'onuCfgOnuRTD': 'rtd', 'onuCfgVendorID': 'vendor', 'onuCfgVersion': 'version', 'onuCfgTrafficManagementOption': 'trafficManagement', 'onuCfgEquipmentID': 'equipmentId', 'onuCfgOmccVersion': 'omccVersion', 'onuCfgOnuHardwareType': 'hardwareType', 'onuCfgOnuHardwareRevision': 'hardwareRevision', 'onuCfgTotalPriorityQueueNumber': 'priorityQueueNum', 'onuCfgTotalTrafficSchedulerNumber': 'trafficSchedulerNum', 'onuCfgTotalGEMPortNumber': 'gemPortNum', 'onuCfgTotalTCONTNumber': 'tcontNum', 'onuCfgTotalEthernetUNINumber': 'ethUniNum', 'onuCfgOnuImageInstance0Version': 'imageInstance0Version', 'onuCfgOnuImageInstance0Valid': 'imageInstance0Valid', 'onuCfgOnuImageInstance0Activate': 'imageInstance0Activate', 'onuCfgOnuImageInstance0Commit': 'imageInstance0Commit', 'onuCfgOnuImageInstance1Version': 'imageInstance1Version', 'onuCfgOnuImageInstance1Valid': 'imageInstance1Valid', 'onuCfgOnuImageInstance1Activate': 'imageInstance1Activate', 'onuCfgOnuImageInstance1Commit': 'imageInstance1Commit', 'onuCfgOnuFastLeaveCapability': 'fastLeaveCapability', 'onuCfgPiggybackDbaRep': 'piggybackDbaRep', 'onuCfgWholeOnuDbaRep': 'wholeOnuDbaRep', 'onuCfgOnuOpticalPowreFeedVoltage': 'powerFeedVoltage', 'onuCfgOnuOpticalReceivedOpticalPower': 'receivedOpticalPower', 'onuCfgOnuOpticallOpticalLaunchPower': 'launchPower', 'onuCfgOnuOpticalLaserBiasCurrent': 'laserBiasCurrent', 'onuCfgOnuOpticalTemperature': 'temperature', 'onuExtCfgPhoneNum': 'phoneNumber', 'onuExtCfgIfDesc3': 'idCard', 'onuExtCfgIfDesc2': 'address', 'onuCfgSerialNumber': 'oldSerialNo', 'onuCfgPassword': 'password', 'onuCfgOnuType': 'onuType', 'onuVirtualPortCfgPortNo': 'portNo', 'onuVirtualPortCfgLogicalPortNo': 'onuId', 'onuVirtualPortCfgVirtualPortNo': 'virtualPortId', 'onuVirtualPortCfgAdministrativeState': 'adminState', 'onuVirtualPortCfgTcontIndex': 'tcontIdnex', 'onuVirtualPortCfgoltVLANTranslationProfileIndex': 'oltTransProIndex', 'onuVirtualPortCfgOltGEMPortNo': 'gemPortNo', 'onuVirtualPortCfgOltAllocID': 'allocId', 'onuVirtualPortCfgOnuMACFilterProfileIndex': 'macFilterProIndex', 'onuVirtualPortCfgOnuMACFilterPreassignProfileIndex': 'macFilterPreassignIndex', 'onuVirtualPortCfgEncryptionMode': 'encryptionMode', 'onuVirtualPortCfgDownstreamRatelimit': 'downstreamRateLimit', 'onuVirtualPortCfgUpstreamRatelimit': 'upstreamRateLimit', 'onuVirtualPortCfgDownstreamBrustSize': 'downstreamBrustSize', 'onuVirtualPortCfgUpstreamBrustSize': 'upstreamBrustSize', 'onuCfgEnablePm': 'enablePM', 'onuCfgBerIntervalConfiguration': 'berInterval', 'onuCfgPowerLevel': 'powerLevel', 'onuCfgBatteryBackup': 'batteryBackup', 'onuCfgAdministrativeState': 'adminState', 'onuExtCfgDisableSerialNumber': 'disableSerialNum', 'onuExtCfgEnableAntiRogueOnu': 'antiRogueOnu', 'onuCfgSecurityMode': 'securityMode', 'onuCfgOnuMacAddress': 'macAddress', 'onuCfgOnuDHCPMode': 'dhcpMode', 'onuCfgOnuIPAddress': 'ipAddress', 'onuCfgOnuIPMask': 'ipMask', 'onuCfgOnuDefaultGateway': 'gateway', 'onuCfgMacLimit': 'macLimit', 'onuCfgFecTxEnable': 'fecTxEnable', 'onuThresholdLowerOpticalPower': 'onuExtCfgLowerOpticalThr', 'onuThresholdUpperOpticalPower': 'onuExtCfgUpperOpticalThr', 'onuThresholdLowerTxPowerThr': 'onuExtCfgLowerTxPowerThr', 'onuThresholdUpperTxPowerThr': 'onuExtCfgUpperTxPowerThr', 'onuCfgFlowProfileIndex': 'flowProf', 'onuCfgTcontVirtualPortBindingProfileIndex': 'tcontVPortBindProf', 'onuEthUniCfgPortNo': 'portNo', 'onuEthUniCfgLogicalPortNo': 'logicalPortNo', 'onuEthUniCfgPhysicalPortNo': 'physicalPortNo', 'onuEthUniCfgAdministrativeState': 'adminState', 'onuEthUniCfgOperationalState': 'operationState', 'onuEthUniCfgmacLimit': 'macLimit', 'onuEthUniCfgLoopback': 'loopback', 'onuEthUniCfgIndConfiguration': 'uniConfiguration', 'onuEthUniCfgSensedType': 'sensedType', 'onuEthUniCfgSpeed': 'speed', 'onuEthUniCfgDuplex': 'duplex', 'onuEthUniCfgExpectedType': 'expectedType', 'onuEthUniCfgMaxFrameSize': 'maxFrameSize', 'onuEthUniCfgIndDTEDCE': 'indDteDce', 'onuEthUniCfgPauseTime': 'pauseTime', 'onuEthUniCfgBridgedIpInd': 'bridgedIpInd', 'onuEthUniCfgArc': 'arc', 'onuEthUniCfgArcInterval': 'arcInterval', 'onuEthUniCfgPppoeFilter': 'pppoeFilter', 'onuEthUniCfgOnuMulticastOperationProfileIndex': 'multiOperProf', 'onuEthUniCfgOnuDynmicMulticastGroupsProfileIndex': 'dynamicMultiProf', 'onuEthUniCfgOnuStaticMulticastGroupsProfileIndex': 'staticMultiProf', 'onuEthUniCfgUsVlanMode': 'usVlanMode', 'onuEthUniCfgDsVlanMode': 'dsVlanMode', 'onuEthUniCfgVid': 'vid', 'onuEthUniCfgPbit': 'priority', 'onuEthUniCfgUsUniRateCir': 'upstreamCir', 'onuEthUniCfgUsUniRatePir': 'upstreamPir', 'onuEthUniCfgDsUniRateCir': 'downstreamCir', 'onuEthUniCfgDsUniRatePir': 'downstreamPir', 'onuEthVlanTransCfgSlotNo': 'slotNo', 'onuEthVlanTransCfgPortNo': 'portNo', 'onuEthVlanTransCfgLogicalPortNo': 'onuId', 'onuEthVlanTransCfgPhysicalPortNo': 'physicalPortList', 'onuEthVlanTransCfgIndex': 'index', 'onuEthVlanTransCfgDownstreamMode': 'downstreamMode', 'onuEthVlanTransCfgInputTPID': 'inputTpid', 'onuEthVlanTransCfgOutputTPID': 'outputTpid', 'onuEthVlanTransCfgFilterOuterPriority': 'filterOuterPriority', 'onuEthVlanTransCfgFilterOuterVID': 'filterOuterVid', 'onuEthVlanTransCfgFilterOuterTPIDDE': 'filterOuterTpidde', 'onuEthVlanTransCfgFilterInnerPriority': 'filterInnerPriority', 'onuEthVlanTransCfgFilterInnerVID': 'filterInnerVid', 'onuEthVlanTransCfgFilterInnerTPIDDE': 'filterInnerTpidde', 'onuEthVlanTransCfgFilterEthertype': 'filterEtherType', 'onuEthVlanTransCfgTreatmentTagsRemove': 'treatmentTagsRemove', 'onuEthVlanTransCfgTreatmentOuterPriority': 'treatmentOuterPriority', 'onuEthVlanTransCfgTreatmentOuterVID': 'treatmentOuterVid', 'onuEthVlanTransCfgTreatmentOuterTPIDDE': 'treatmentOuterTpidde', 'onuEthVlanTransCfgTreatmentInnerPriority': 'treatmentInnerPriority', 'onuEthVlanTransCfgTreatmentInnerVID': 'treatmentInnerVid', 'onuEthVlanTransCfgTreatmentInnerTPIDDE': 'treatmentInnerTpidde', 'onuEthVlanTransCfgTreatmentTagsMode': 'treatmentTagsMode', 'actLinkPortId': 'portNo', 'onuPortVlanProfPortNo': 'portNo', 'onuPortVlanProfLogicalPortNo': 'onuId', 'onuPortVlanProfPhysicalPortNo': 'physicalPortId', 'onuPortVlanProfIndex': 'profIndex', 'onuPortVlanProfFilterOuterPri': 'filterOuterPriority', 'onuPortVlanProfFilterOuterVid': 'filterOuterVid', 'onuPortVlanProfFilterOuterTpid': 'filterOuterTpid', 'onuPortVlanProfFilterInnerPri': 'filterInnerPriority', 'onuPortVlanProfFilterInnerVid': 'filterInnerVid', 'onuPortVlanProfFilterInnerTpid': 'filterInnerTpid', 'onuPortVlanProfFilterEtherType': 'filterEtherType', 'onuPortVlanProfTreatmentOuterPri': 'treatmentOuterPriority', 'onuPortVlanProfTreatmentOuterVid': 'treatmentOuterVid', 'onuPortVlanProfTreatmentOuterTpid': 'treatmentOuterTpid', 'onuPortVlanProfTreatmentInnerPri': 'treatmentInnerPriority', 'onuPortVlanProfTreatmentInnerVid': 'treatmentInnerVid', 'onuPortVlanProfTreatmentInnerTpid': 'treatmentInnerTpid', 'onuPortVlanProfTreatmentTagToRemove': 'treatmentTagsRemove', 'onuPortVlanProfMode': 'profMode', 'onuPortVlanProfAction': 'profAction', 'onuPortVlanProfDownstream': 'profDownStream', 'onuPortVlanProfInputTPID': 'inputTpid', 'onuPortVlanProfOutputTPID': 'outputTpid', 'onuDynamicStatusPortNo': 'portNo', 'onuDynamicStatusLogicalPortNo': 'onuId', 'onuDynamicStatusOnuDeactiveReason': 'status', 'onuBlackListSlotNo': 'slotNo', 'onuBlackListPortNo': 'portNo', 'onuBlackListPassword': 'password', 'onuBlackListSerialNumber': 'serialNum', 'onuBlackListCause': 'cause', 'onuBlackListRegistrationId': 'password', 'oltPonLinkSetCfgLinkSetId': 'setId', 'oltPonLinkSetCfgName': 'name', 'oltPonLinkSetCfgLinkSetType': 'setType', 'oltPonLinkSetCfgSwitchOverTimeout': 'switchOverTime', 'oltPonLinkSetCfgForceSwitch': 'forceSwitch', 'oltPonLinkSetCfgLink1SlotId': 'link1SlotId', 'oltPonLinkSetCfgLink1PortId': 'link1PortId', 'oltPonLinkSetCfgLink2SlotId': 'link2SlotId', 'oltPonLinkSetCfgLink2PortId': 'link2PortId', 'oltPonLinkSetCfgActLinkSlotId': 'actLinkSlotId', 'oltPonLinkSetCfgActLinkPortId': 'actLinkPortId', 'oltPonLinkSetCfgVirtualLinkSlotId': 'virtualLinkSlotId', 'oltPonLinkSetCfgVirtualLinkPortId': 'virtualLinkPortId', 'oltOntCounterPortNo': 'portNo', 'oltOntCounterLogicalPortNo': 'onuNo', 'onuGemPortCounterPortNo': 'portNo', 'onuGemPortCounterLogicalPortNo': 'onuNo', 'oltPonLinkPmPortNo': 'portNo', 'oltPonLinkPmIntervalID': 'intervalId', 'gponGemPortPmTableTime': 'gponOntPmStartTime', 'oltPonLinkPmRxGem': 'rxGem', 'oltPonLinkPmRxGemDropped': 'rxGemDropped', 'oltPonLinkPmRxGemIdle': 'rxGemIdle', 'oltPonLinkRxGemCorrected': 'rxGemCorrected', 'oltPonLinkPmRxGemIllegal': 'rxGemIllegal', 'oltPonLinkPmRxAllocationsValid': 'rxAllocationsValid', 'oltPonLinkPmRxAllocationsInvalid': 'rxAllocationsInvalid', 'oltPonLinkPmRxAllocationsDisabled': 'rxAllocationsDisabled', 'oltPonLinkPmRxPloams': 'rxPloams', 'oltPonLinkPmRxPloamsNonIdle': 'rxPloamsNonIdle', 'oltPonLinkPmRxPloamsError': 'rxPloamsError', 'oltPonLinkPmRxPloamsDropped': 'rxPloamsDropped', 'oltPonLinkPmRxCpu': 'rxCpu', 'oltPonLinkPmRxOmci': 'rxOmci', 'oltPonLinkPmRxDroppedTooShort': 'rxDroppedTooShort', 'oltPonLinkPmRxDroppedTooLong': 'rxDroppedTooLong', 'oltPonLinkPmRxCrcErrors': 'rxCrcErrors', 'oltPonLinkPmRxKeyErrors': 'rxKeyErrors', 'oltPonLinkPmRxFragmentsErrors': 'rxFragmentsError', 'oltPonLinkPmRxPacketsDropped': 'rxPacketsDropped', 'oltPonLinkPmTxGem': 'txGem', 'oltPonLinkPmTxPloams': 'txPloams', 'oltPonLinkPmTxGemFragments': 'txGemFragments', 'oltPonLinkPmTxCpu': 'txCpu', 'oltPonLinkPmTxOmci': 'txOmci', 'oltPonLinkPmTxCpuOmciPacketsDropped': 'txCpuOmciPacketsDropped', 'oltPonLinkPmTxDroppedIllegalLength': 'txDroppedIllegalLength', 'oltPonLinkPmTxDroppedTpidMiss': 'txDroppedTpidMiss', 'oltPonLinkPmTxDroppedVidMiss': 'txDroppedVidMiss', 'gponOntPmPortNo': 'portNo', 'gponOntPmLogicalPortNo': 'onuNo', 'gponGemPortPmPortNo': 'portNo', 'gponGemPortPmLogicalPortNo': 'onuNo', 'gponGemPortPmVirtualPortNo': 'physicalPort', 'gponGemPortPmIntervalID': 'intervalId', 'gponGemPortPmTxTotalFrames': 'txFrames', 'gponGemPortPmTxTotalBytes': 'txBytes', 'gponGemPortPmRxTotalFrames': 'rxFrames', 'gponGemPortPmRxTotalBytes': 'rxBytes', 'onuNniPmHistoryDataSlotNo': 'slotNo', 'onuNniPmHistoryDataPortNo': 'portNo', 'onuNniPmHistoryDataLogicalPortNo': 'onuNo', 'oltNNICounterSlotNo': 'slotNo', 'oltNNICounterPortNo': 'portNo', 'oltPonLinkCounterPortNo': 'portNo', 'oltPonLinkCounterRxBandWidthUtilization': 'utsEthIfLoadStatsRxBandwidthPercent', 'oltPonLinkCounterTxBandWidthUtilization': 'utsEthIfLoadStatsTxBandwidthPercent', 'onuFlowProfIndex1': 'index1', 'onuFlowProfIndex2': 'index2', 'onuFlowProfileName': 'name', 'onuFlowProfUniType': 'uniType', 'onuFlowProfUniPortBitMap': 'uniPortBitMap', 'onuFlowProfUpstreamMapType': 'upstreamMapType', 'onuFlowProfVlanIDStart': 'vlanIdStart', 'onuFlowProfVlanIDStop': 'vlanIdStop', 'onuFlowProfPriorityBitMap': 'priorityBitMap', 'onuFlowProfVirtualPortNo': 'virtualPortNo', 'schedulerProfileIndex': 'index', 'profileName': 'name', 'onuVPortSvcProfileIndex': 'index', 'onuVPortSvcProfileName': 'name', 'onuVPortSvcProfUpstreamFlowPriority': 'upstreamFlowPriority', 'bandwidthProfileIndex': 'index', 'onuBwProfileName': 'name', 'maximumBandwidth': 'maxBandwidth', 'onuTcontServiceProfileIndex': 'index', 'onuTcontSvcProfileName': 'name', 'onuBwBean': 'bwBean', 'upstreamQueuingSchedulingType': 'type', 'tcontVirtualPortBindingProfileIndex': 'index', 'tcontVirtualPortBindingProfileVirtualPortNo': 'virtualPortNo', 'onuTcontVPortBindProfileName': 'name', 'onuEthUniCfgProEthernetUNIProfileIndex': 'index', 'onuEthUniCfgProProfileName': 'name', 'onuEthUniCfgProAutoNegotiation': 'autoNegotiation', 'onuEthUniCfgProSpeed': 'speed', 'onuEthUniCfgProDuplex': 'duplex', 'onuEthUniCfgProExpectedType': 'type', 'onuEthUniCfgProMaxFrameSize': 'maxFrameSize', 'onuEthUniCfgProIndDTEDCE': 'dtedce', 'onuStaticMultiGroupProfIndex1': 'index1', 'onuStaticMultiGroupProfIndex2': 'index2', 'onuStaticMultiGroupProfileName': 'name', 'onuStaticMultiGroupProfMulticastGemPortNo': 'gemPortNo', 'onuStaticMultiGroupProfMulticastVLANID': 'vlanId', 'onuStaticMultiGroupProfSourceIPAddress': 'sourceIpAddress', 'onuStaticMultiGroupProfMulticastGroupAddressStart': 'groupAddressStart', 'onuStaticMultiGroupProfMulticastGroupAddressStop': 'groupAddressStop', 'onuStaticMultiGroupProfImputedGroupBandwidth': 'bandwidth', 'onuDynamicMultiGroupProfIndex1': 'index1', 'onuDynamicMultiGroupProfIndex2': 'index2', 'onuDynamicMultiGroupProfileName': 'name', 'onuDynamicMultiGroupProfMulticastGemPortNo': 'gemPortNo', 'onuDynamicMultiGroupProfMulticastVLANID': 'vlanId', 'onuDynamicMultiGroupProfSourceIPAddress': 'sourceIpAddress', 'onuDynamicMultiGroupProfMulticastGroupAddressStart': 'groupAddressStart', 'onuDynamicMultiGroupProfMulticastGroupAddressStop': 'groupAddressStop', 'onuDynamicMultiGroupProfImputedGroupBandwidth': 'bandwidth', 'onuDynamicMultiGroupProfMulticastGroupIpv6AddressStart': 'groupIpv6AddressStart', 'onuDynamicMultiGroupProfMulticastGroupIpv6AddressStop': 'groupIpv6AddressStop', 'onuMulticastOperProfileIndex': 'index', 'onuMulticastOperProfileName': 'name', 'onuMulticastOperProfIgmpVersion': 'igmpVersion', 'onuMulticastOperProfMulticastControlMode': 'multicastControlMode', 'onuMulticastOperProfFastLeaveMode': 'fastLeaveMode', 'onuMulticastOperProfUpstreamIGMPTagControl': 'upstreamIgmpTag', 'onuMulticastOperProfUpstreamIGMPTCIPbits': 'upstreamIgmpPbits', 'onuMulticastOperProfMaxSimultaneousGroup': 'maxSimultaneousGroup', 'onuMulticastOperProfDownstreamIgmpMstTagControl': 'downstreamTag', 'onuMulticastOperProfDownstreamIgmpMcastTCIPbits': 'downstreamPbits', 'onuSIPAgentProfileIndex': 'index', 'onuSIPAgentProfileName': 'name', 'onuSIPAgentProfileProxySrvAddr': 'proxyAddress', 'onuSIPAgentProfileOutProxyAddr': 'outProxyAddress', 'onuSIPAgentProfileSipRegistrar': 'sipRegistrar', 'onuSIPAgentProfileSoftSwitchVendor': 'softSwitchVendor', 'onuSIPAgentProfileTcpPort': 'tcpPort', 'onuPotsUniCfgPortNo': 'portId', 'onuPotsUniCfgLogicalPortNo': 'onuId', 'onuPotsUniCfgPhysicalPortNo': 'potsId', 'onuPotsUniCfgsipAgentProfileIndex': 'sipProf', 'gnOnuWanPPPoEConfigProfilePortNo': 'portId', 'gnOnuWanPPPoEConfigProfileLogicalPortNo': 'onuId', 'gnOnuWanPPPoEConfigProfileIndex': 'index', 'gnOnuWanPPPoEConfigProfileUserName': 'userName', 'gnOnuWanPPPoEConfigProfilePassword': 'password', 'gnOnuWanPPPoEConfigProfileServiceName': 'serviceName', 'gnOnuWanPPPoEConfigProfileDialMode': 'mode', 'gnOnuWanIpConfigProfilePortNo': 'portId', 'gnOnuWanIpConfigProfileLogicalPortNo': 'onuId', 'gnOnuWanIpConfigProfileIndex': 'index', 'gnOnuWanIpConfigProfileIpaddress': 'ipAddress', 'gnOnuWanIpConfigProfileIpMask': 'ipMask', 'gnOnuWanIpConfigProfileGateway': 'gateway', 'gnOnuWanIpConfigProfilePrimaryDns': 'primaryDns', 'gnOnuWanIpConfigProfileSecondaryDns': 'secondaryDns', 'gnOnuWanConfigDataPortNo': 'portId', 'gnOnuWanConfigDataLogicalPortNo': 'onuId', 'gnOnuWanConfigDataWanIndex': 'index', 'gnOnuWanConfigDataConnectionName': 'connectionName', 'gnOnuWanConfigDataMode': 'mode', 'gnOnuWanConfigDataProtocolMode': 'protocolType', 'gnOnuWanConfigDataIpOpt': 'operationType', 'gnOnuWanConfigData8021p': 'data8021p', 'gnOnuWanConfigDataServiceMode': 'serviceMode', 'gnOnuWanConfigDataVlanId': 'vlanId', 'gnOnuWanConfigDataPortBinding': 'portBinding', 'gnOnuWanConfigDataIpProfileIndex': 'ipProfileIndex', 'gnOnuWanConfigDataPPPoEProfileIndex': 'pppoeProfileIndex', 'gnOnuWanConfigNumPortNo': 'portId', 'gnOnuWanConfigNumLogicalPortNo': 'onuId', 'gnOnuWanConfigNum': 'number', 'gponSysCfgAuthenticationMethod': 'authMethod', 'oltPonLinkCfgPortNo': 'portNo', 'oltPonLinkCfgLinkSetId': 'linkSetId', 'oltPonLinkCfgAdministrativeState': 'adminState', 'oltPonLinkCfgOperationalState': 'operationalState', 'oltPonLinkCfgOnuDiscoveryMode': 'onuDiscoveryState', 'oltPonLinkCfgOnuDiscoveryInterval': 'onuDiscoveryInterval', 'oltPonLinkCfgCycleTime': 'cycleTime', 'oltPonLinkCfgBroadcastGEMPortNo': 'broadcastGemPort', 'oltPonLinkCfgLosThreshold': 'losThreshold', 'oltPonLinkCfgLofThreshold': 'lofThreshold', 'oltPonLinkCfgAutoUpgradeEnable': 'autoUpgrade', 'oltPonLinkCfgKeyExchange': 'keyExchange', 'oltPonLinkCfgKeyExchangeInterval': 'keyExchangeInterval', 'oltPonLinkCfgFecTxEnable': 'fecTxEnable', 'oltPonLinkRogueOnuOperState': 'rogueOnuState', 'oltPonLinkRogueOnuOperMode': 'rogueOnuMode', 'oltPonLinkPonMaxDistance': 'maxDistance', 'oltPonLinkCfgEnablePm': 'enable', 'onuUpgradeParticipantPortListBitMap': 'participantPortListBitMap', 'onuUpgradeProgressDownloadPortListBitMap': 'downloadPortListBitMap', 'onuUpgradeProgressCommitPortListBitMap': 'commitPortListBitMap', 'onuUpgradeProgressActivatePortListBitMap': 'activatePortListBitMap', 'onuUpgradeProgressFinalPortListBitMap': 'finalPortListBitMap', 'onuUpgradeResultPortListBitMap': 'resultPortListBitMap', 'eqptId': 'equipmentId', 'onuUpgradeImageVersion': 'imageVersion', 'firmwareName': 'imageName', 'onuSwDlPolilcyPortListBitMap': 'ponList', 'onuUpgradeScheduleTime': 'timeStart', 'onuUpgradeTaskandResultPortNo': 'ponPort', 'onuUpgradeTaskandResultEqptId': 'equipmentId', 'onuUpgradeTaskandResultImageName': 'imageName', 'onuUpgradeTaskandResulttimestamp': 'timeStart', 'onuUpgradeTaskandResultAllOnuStatus': 'progressState', 'upgradeONUList': 'onuList', 'upgradeONU': 'onuUpgradeStateList', 'onuUpgradeTaskandResultschedule': 'autoEnable', 'oltOpmSwitch': 'pmSwitch', 'oltOpmStartHour': 'startHour', 'oltOpmStartMinute': 'startMinute', 'oltOpmPeriod': 'period', 'oltOpmOltBitmap': 'oltBitMap', 'oltOpmOnuBitmap': 'onuBitMap', 'oltOpmVoltageMinAlarmThreshold': 'voltageLowAlarm', 'oltOpmVoltageClearMinAlarmThreshold': 'voltageLowAlarmClear', 'oltOpmVoltageMaxAlarmThreshold': 'voltageHighAlarm', 'oltOpmVoltageClearMaxAlarmThreshold': 'voltageHighAlarmClear', 'oltOpmVoltageMinWarningThreshold': 'voltageLowWarn', 'oltOpmVoltageClearMinWarningThreshold': 'voltageLowWarnClear', 'oltOpmVoltageMaxWarningThreshold': 'voltageHighWarn', 'oltOpmVoltageClearMaxWarningThreshold': 'voltageHighWarnClear', 'oltOpmBiasCurrentMinAlarmThreshold': 'currentLowAlarm', 'oltOpmBiasCurrentClearMinAlarmThreshold': 'currentLowAlarmClear', 'oltOpmBiasCurrentMaxAlarmThreshold': 'currentHighAlarm', 'oltOpmBiasCurrentClearMaxAlarmThreshold': 'currentHighAlarmClear', 'oltOpmBiasCurrentMinWarningThreshold': 'currentLowWarn', 'oltOpmBiasCurrentClearMinWarningThreshold': 'currentLowWarnClear', 'oltOpmBiasCurrentMaxWarningThreshold': 'currentHighWarn', 'oltOpmBiasCurrentClearMaxWarningThreshold': 'currentHighWarnClear', 'oltOpmTemperatureMinAlarmThreshold': 'tempLowAlarm', 'oltOpmTemperatureClearMinAlarmThreshold': 'tempLowAlarmClear', 'oltOpmTemperatureMaxAlarmThreshold': 'tempHighAlarm', 'oltOpmTemperatureClearMaxAlarmThreshold': 'tempHighAlarmClear', 'oltOpmTemperatureMinWarningThreshold': 'tempLowWarn', 'oltOpmTemperatureClearMinWarningThreshold': 'tempLowWarnClear', 'oltOpmTemperatureMaxWarningThreshold': 'tempHighWarn', 'oltOpmTemperatureClearMaxWarningThreshold': 'tempHighWarnClear', 'oltOpmTxPowerMinAlarmThreshold': 'txPowerLowAlarm', 'oltOpmTxPowerClearMinAlarmThreshold': 'txPowerLowAlarmClear', 'oltOpmTxPowerMaxAlarmThreshold': 'txPowerHighAlarm', 'oltOpmTxPowerClearMaxAlarmThreshold': 'txPowerHighAlarmClear', 'oltOpmTxPowerMinWarningThreshold': 'txPowerLowWarn', 'oltOpmTxPowerClearMinWarningThreshold': 'txPowerLowWarnClear', 'oltOpmTxPowerMaxWarningThreshold': 'txPowerHighWarn', 'oltOpmTxPowerClearMaxWarningThreshold': 'txPowerHighWarnClear', 'oltOpmRxPowerMinAlarmThreshold': 'rxPowerLowAlarm', 'oltOpmRxPowerClearMinAlarmThreshold': 'rxPowerLowAlarmClear', 'oltOpmRxPowerMaxAlarmThreshold': 'rxPowerHighAlarm', 'oltOpmRxPowerClearMaxAlarmThreshold': 'rxPowerHighAlarmClear', 'oltOpmRxPowerMinWarningThreshold': 'rxPowerLowWarn', 'oltOpmRxPowerClearMinWarningThreshold': 'rxPowerLowWarnClear', 'oltOpmRxPowerMaxWarningThreshold': 'rxPowerHighWarn', 'oltOpmRxPowerClearMaxWarningThreshold': 'rxPowerHighWarnClear', 'oltPonLinkOpticalBaseInfoPortNo': 'portId', 'oltPonLinkOpticalBaseInfoTransType': 'transType', 'oltPonLinkOpticalBaseInfoConnectorType': 'connectorType', 'oltPonLinkOpticalBaseInfoWaveLength': 'waveLength', 'oltPonLinkOpticalBaseInfoVendorName': 'vendorName', 'oltPonLinkOpticalBaseInfoVendorPartNumber': 'vendorPartNum', 'oltPonLinkOpticalBaseInfoVendorSerialNumber': 'vendorSerialNum', 'oltPonLinkOpticalBaseInfoManufacturingDate': 'manufacturingDate', 'oltPonLinkOpticalBaseInfoDDM': 'ddm', 'oltPonLinkOpticalBaseInfoXGWaveLength': 'xgWaveLength', 'sliceName': 'name', 'sliceManagerIP': 'ipAddress', 'neId': 'oltId', 'sliceId': 'oltSliceId', 'sliceMode': 'mode', 'sliceNeUserList': 'neUserList', 'sliceUplinkMember': 'uplinkPortList'}


def childData():
    # 创建一个空字典，用于存储合并后的数据
    merged_data = {}
    # 遍历指定目录下的所有JSON文件
    directory = "new_json"
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    newKey = key.replace("Table", "")
                    if "nodetype" in value and value["nodetype"] == "table":
                        table_data = {k: v for k, v in value.items() if not isinstance(v, dict)}
                        table_child = {}
                        for k, v in value.items():
                            if isinstance(v, dict):
                                # oid_value = v.pop("oid", None)
                                oid_value = v["oid"]
                                # if "ProfileName" in v["name"] or "profileName" in v["name"]:
                                #     v["name"] = "name"
                                # if "ProfileIndex" in v["name"] or "profileIndex" in v["name"]:
                                #     v["name"] = "index"

                                # v["name"] = v["name"].replace(newKey, "")
                                # if v["name"]:
                                #     v["name"] = low_first(v["name"])

                                v.pop("nodetype", None)
                                v.pop("oid", None)
                                if oid_value is not None:
                                    j = oid_value.rsplit(".", 1)[-1]
                                    table_child[j] = v
                        table_data["child"] = table_child
                        table_data.pop("name", None)
                        merged_data[key] = table_data
    # 将合并后的数据写入一个新的JSON文件
    output_file = "merged_data5.json"
    with open(output_file, "w") as outfile:
        json.dump(merged_data, outfile, indent=4)

    print("JSON files merged and saved to", output_file)

def mergeData():
    # 存储所有JSON数据的列表
    all_data = []

    # 遍历指定目录下的所有JSON文件
    directory = "new_json"
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                all_data.append(data)

    # 将所有数据合并为一个列表
    merged_data = []
    for data in all_data:
        merged_data.extend(data)

    # 写入合并后的数据到新的JSON文件
    output_file = "merged_data.json"
    with open(output_file, "w") as outfile:
        json.dump(merged_data, outfile, indent=4)

    print("All JSON files merged and saved to", output_file)


def update_json_file(file_path, file_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    tables = {key: value for key, value in data.items() if
              isinstance(value, dict) and "Table" in key and "oid" in value}
    objects = [value for value in data.values() if isinstance(value, dict) and "oid" in value]
    updated_tables = {}  # 创建一个新字典来存储更新后的表格数据
    # table_objects = [{**obj, "oid": obj["oid"][obj["oid"].rfind(".") + 1:]} for obj in objects if table_value["oid"] in obj["oid"] and obj["oid"].count(".") - table_value["oid"].count(".") == 2]
    for table_key, table_value in tables.items():
        table_objects = []
        for obj in objects:
            if (len(table_value["oid"]) + 1 < len(obj["oid"])):
                if (table_value["oid"] == obj["oid"][:len(table_value["oid"])] and
                    obj["oid"].count(".") - table_value["oid"].count(".") == 2) and obj["oid"][
                    len(table_value["oid"])] == ".":
                    table_objects.append(obj)

        updated_table = {obj["name"]: obj for obj in table_objects}
        updated_tables[table_key] = {**table_value, **updated_table}  # 更新表格数据
    with open(f'new_json/{file_name}', 'w') as j_file:
        json.dump(updated_tables, j_file, indent=4)


def getData():
    # 指定包含JSON文件的文件夹路径
    folder_path = 'json'

    # 获取文件夹中所有文件的文件名列表
    file_names = os.listdir(folder_path)

    # 遍历文件夹中的每个文件
    for file_name in file_names:
        # 拼接文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        print(file_name)

        # 检查文件是否为JSON文件
        if file_name.endswith('.json'):
            # 打开JSON文件并加载数据
            with open(file_path, 'r') as file:
                # json_data = json.load(file)
                file_path = os.path.join(folder_path, file_name)
                update_json_file(file_path, file_name)
                # 处理加载的JSON数据，这里只是简单打印
                # print(json_data)


# childData()
# with open('json/GENEW-FM-MIB.json', 'r') as file:
#     data = json.load(file)
#
# tables = {key: value for key, value in data.items() if isinstance(value, dict) and "Table" in key and "oid" in value}
# objects = [value for value in data.values() if isinstance(value, dict) and "oid" in value]
#
# updated_tables = {}  # 创建一个新字典来存储更新后的表格数据
#
# for table_key, table_value in tables.items():
#     table_objects = [obj for obj in objects if table_value["oid"] in obj["oid"]]
#     updated_table = {obj["name"]: obj for obj in table_objects}
#     updated_tables[table_key] = {**table_value, **updated_table}  # 更新表格数据
#
#
# # pprintpp.pprint(updated_tables)
#
# # # 将更新后的表格数据写入新的 JSON 文件
# with open('new_json/updated_tables.json', 'w') as j_file:
#     json.dump(updated_tables, j_file)


# with open("OnuRateControlSchedulerProfTable.java_file", 'r') as file:
#     data = file.read()
#     print(data)

def getJavaData():
    # 初始化一个列表来存储截取的内容
    datas = {}
    # 指定包含JSON文件的文件夹路径
    folder_path = 'java_file'

    # 获取文件夹中所有文件的文件名列表
    file_names = os.listdir(folder_path)

    # 遍历文件夹中的每个文件
    for file_name in file_names:
        # 拼接文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        print(file_name)

        # 检查文件是否为JSON文件
        if file_name.endswith('.java'):
            # 打开JSON文件并加载数据
            with open(file_path, 'r') as file:
                # json_data = json.load(file)
                file_path = os.path.join(folder_path, file_name)
                test(file_path, datas)
                # 处理加载的JSON数据，这里只是简单打印
                # print(json_data)
    with open(f'new_java/1g.json', 'w') as j_file:
        json.dump(datas, j_file, indent=4)


def test(file_path, datas):
    java_file_path = file_path
    # 初始化一个列表来存储截取的内容
    contents = []
    tableoid = ""
    # 定义正则表达式模式
    # pattern_braces = r'\{([^{}]+)\}'

    # 定义正则表达式模式
    pattern_init_table = r'/\*+\s*\*/\s*public class (\w+)'
    pattern_init_braces = r'init\(\) \{([^{}]+)\}'
    pattern_retrieve_braces = r'retrieve\(\) throws Exception \{([^{}]+)\}'

    pattern_snmp = r'initProperty\("(.*?)",\s*new SnmpMibBeanProperty\(".*?",\s*"(.*?)",\s*(\d+)\)'
    pattern_retrieve = r'getProperty\("(.*?)"\)'
    # 打开Java文件并读取内容
    with open(java_file_path, 'r') as file:
        java_code = file.read()

    # 使用正则表达式截取特定字符串开头的花括号内的内容
    matches_init = re.finditer(pattern_init_table, java_code)
    for match in matches_init:
        contents.append(match.group(1))
    newKey = low_first(contents[0].replace("Table", ""))
    replace_uts ="uts" + contents[0].replace("Table", "")
    matches_init = re.finditer(pattern_init_braces, java_code)
    for match in matches_init:
        fields = {}
        for match1 in re.finditer(pattern_snmp, match.group(1)):
            field_name, field_oid, field_type = match1.groups()
            j = field_oid.rsplit(".")
            if tableoid == "": tableoid = ".".join(j[:-2])
            # if "ProfileName" in field_name or "profileName" in field_name:
            #     field_name = "name"
            # if "ProfileIndex" in field_name or "profileIndex" in field_name:
            #     field_name = "index"

            # field_name = field_name.replace(newKey, "").replace(replace_uts, "")
            # if field_name:
            #     field_name = low_first(field_name)
            if field_name in childkeys:
                field_name = childkeys[field_name]
            type = 4 if int(field_type) == 100 else int(field_type)
            fields[j[-1]] = {"name": field_name, "type": type}
        contents.append(fields)

    matches_retrieve = re.finditer(pattern_retrieve_braces, java_code)
    for match in matches_retrieve:
        fields = []
        for match1 in re.finditer(pattern_retrieve, match.group(1)):
            value = match1.group(1)
            # if "ProfileName" in value or "profileName" in value:
            #     value = "name"
            # if "ProfileIndex" in value or "profileIndex" in value:
            #     value = "index"
            fields.append(value.replace(newKey, ""))
        contents.append(fields)
    print(contents)
    # if contents[0] == "OnuVPortSvcProfTable":
    #     contents[0] = "VirtualPortServiceProfile"
    # elif contents[0] == "OnuRateControlSchedulerProfTable":
    #     contents[0] = "RateControlProfile"
    # elif contents[0] == "IanModuleEntityTable":
    #     contents[0] = "BoardInformation"
    if len(contents) == 3:
        datas[contents[0]] = {"oid": tableoid[1:], "child": contents[1], "retrieve": contents[2]}
    else:
        datas[contents[0]] = {"oid": tableoid[1:], "child": contents[1]}
    # # 输出截取的内容
    # for content in contents:
    #     # 使用正则表达式提取字段信息
    #     print(content)
    # print(fields)


# childData()
# getJavaData()
getJavaData()

def translate_file():
    # t1 = open("new_java/1.json", 'r')
    # javaData = json.load(t1)
    #
    # t1 = open("merged_data4.json", 'r')
    # all_data = json.load(t1)
    #
    # for data in all_data:
    #     value = all_data[data]
    #     for d in javaData:
    #         v = javaData[d]
    #         if value["oid"] == v["oid"]:
    #             print(v)

    contents = []
    t1 = open("60.async.js", 'r')
    text = t1.read()
    # 定义正则表达式模式
    pattern = r' = \{\s*tableId:.*?\};'
    # 使用正则表达式查找匹配项
    for match in re.finditer(pattern, text, re.DOTALL):
        t = match.group(0)
        m = t.replace("var r=", "").replace(";", "")
        contents.append(t)

    with open(f'new_java/2.json', 'w') as j_file:
        json.dump(contents, j_file, indent=4)

    x = open("new_java/3.js", 'w')
    tt = open("new_java/2.json", 'r')
    tm = json.load(tt)
    for t in tm:
        m = t.replace("var r =", "").replace(";", "")
        # print(m)
        x.write(f"\n{m},")

def tabel_column():
    new_data = {}
    new_data2 = {}
    file = open("new_java/d4.json", 'r', encoding='UTF-8')
    data = json.load(file)
    for d in data:
        column = []
        column2 = []
        for c in d["fields"]:
            line = c
            line["dataIndex"] = c["id"]
            line["title"] = c["display"][0]
            column.append(line)
            column2.append(c["id"])
        new_data[d["tableId"]] = {"columns": column}
        new_data2[d["tableId"]] = column2
    print(new_data)
    # # # 将更新后的表格数据写入新的 JSON 文件
    with open('new_java/column_dataz.json', 'w', encoding='utf-8') as j_file:
        json.dump(new_data, j_file, ensure_ascii=False, indent=4)
    with open('new_java/column_dataz2.json', 'w', encoding='utf-8') as j_file:
        json.dump(new_data2, j_file, ensure_ascii=False, indent=4)