<?php

$catid = 1;
$deviceArr = array(1,2);
$limit = 20;
$page = 1;
$offset = $limit * ($page - 1);
$keyword = 'hello';

require_once 'sphinxapi.php';
$scl = new SphinxClient();
$scl->SetServer('127.0.0.1', 9312);

$scl->SetFilter('status', array(1));
$scl->SetFilter('catid', array($catid));
$scl->SetFilter('support_device', $deviceArr);
$scl->SetLimits($offset, $limit);
$scl->SetSortMode(SPH_SORT_EXTENDED, "id desc");

$res = $scl->Query($keyword, 'idx_app');

var_dump($res['matches']);