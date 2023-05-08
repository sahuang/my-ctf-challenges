export memory memory(initial: 256, max: 32768);

global g_a:int = 65536;
global g_b:int = 0;
global g_c:int = 0;
global g_d:int = 0;

export table indirect_function_table:funcref(min: 1, max: 1);

data d_Tm0m3n7(offset: 65536) = "@Tm0m3n7!\00";

export function wasm_call_ctors() {
  emscripten_stack_init()
}

function f_b(a:int):int {
  var i:int;
  var b:int = g_a;
  var c:int = 16;
  var d:int = b - c;
  d[3]:int = a;
  var e:int = d[3]:int;
  var o:double = f64_convert_i32_s(e);
  var p:double = sqrt(o);
  d[0]:double = p;
  var q:double = d[0]:double;
  var r:double = d[0]:double;
  var s:double = abs(r);
  var t:double = 2147483648.0;
  var f:int = s < t;
  var g:int = eqz(f);
  if (g) goto B_b;
  var h:int = i32_trunc_f64_s(r);
  i = h;
  goto B_a;
  label B_b:
  var j:int = -2147483648;
  i = j;
  label B_a:
  var k:int = i;
  var u:double = f64_convert_i32_s(k);
  var l:int = q == u;
  var m:int = 1;
  var n:int = l & m;
  return n;
}

function f_c(a:int):int {
  var b:int = g_a;
  var c:int = 16;
  var d:int = b - c;
  d[2]:int = a;
  var e:int = d[2]:int;
  var f:int = 1;
  var g:int = e;
  var h:int = f;
  var i:int = g == h;
  var j:int = 1;
  var k:int = i & j;
  if (eqz(k)) goto B_b;
  var l:int = 0;
  var m:int = 1;
  var n:int = l & m;
  d[15]:byte = n;
  goto B_a;
  label B_b:
  var o:int = d[2]:int;
  var p:int = 2;
  var q:int = o;
  var r:int = p;
  var s:int = q == r;
  var t:int = 1;
  var u:int = s & t;
  if (eqz(u)) goto B_c;
  var v:int = 1;
  var w:int = 1;
  var x:int = v & w;
  d[15]:byte = x;
  goto B_a;
  label B_c:
  var y:int = d[2]:int;
  var z:int = 2;
  var aa:int = y % z;
  if (aa) goto B_d;
  var ba:int = 0;
  var ca:int = 1;
  var da:int = ba & ca;
  d[15]:byte = da;
  goto B_a;
  label B_d:
  var ea:int = 3;
  d[1]:int = ea;
  loop L_f {
    var fa:int = d[1]:int;
    var ga:int = d[1]:int;
    var ha:int = fa * ga;
    var ia:int = d[2]:int;
    var ja:int = ha;
    var ka:int = ia;
    var la:int = ja <= ka;
    var ma:int = 1;
    var na:int = la & ma;
    if (eqz(na)) goto B_e;
    var oa:int = d[2]:int;
    var pa:int = d[1]:int;
    var qa:int = oa % pa;
    if (qa) goto B_g;
    var ra:int = 0;
    var sa:int = 1;
    var ta:int = ra & sa;
    d[15]:byte = ta;
    goto B_a;
    label B_g:
    var ua:int = d[1]:int;
    var va:int = 2;
    var wa:int = ua + va;
    d[1]:int = wa;
    continue L_f;
  }
  unreachable;
  label B_e:
  var xa:int = 1;
  var ya:int = 1;
  var za:int = xa & ya;
  d[15]:byte = za;
  label B_a:
  var ab:int = d[15]:ubyte;
  var bb:int = 1;
  var cb:int = ab & bb;
  return cb;
}

function f_d(a:int):int {
  var b:int = g_a;
  var c:int = 16;
  var d:int_ptr = b - c;
  d[3] = a;
  var e:int = d[3];
  var f:int = 0;
  var g:int = e;
  var h:int = f;
  var i:int = g > h;
  var j:int = 0;
  var k:int = 1;
  var l:int = i & k;
  var m:int = j;
  if (eqz(l)) goto B_a;
  var n:int = d[3];
  var o:int = 2;
  var p:int = n % o;
  var q:int = 0;
  m = q;
  if (p) goto B_a;
  var r:int = d[3];
  var s:int = 7;
  var t:int = r % s;
  var u:int = 0;
  var v:int = t;
  var w:int = u;
  var x:int = v == w;
  m = x;
  label B_a:
  var y:int = m;
  var z:int = 1;
  var aa:int = y & z;
  return aa;
}

function f_e(a:int, b:int):int {
  var c:int = g_a;
  var d:int = 16;
  var e:int_ptr = c - d;
  e[3] = a;
  e[2] = b;
  var f:int = e[3];
  var g:int = 10;
  var h:int = f;
  var i:int = g;
  var j:int = h < i;
  var k:int = 0;
  var l:int = 1;
  var m:int = j & l;
  var n:int = k;
  if (eqz(m)) goto B_a;
  var o:int = e[2];
  var p:int = 10;
  var q:int = o;
  var r:int = p;
  var s:int = q < r;
  var t:int = 0;
  var u:int = 1;
  var v:int = s & u;
  n = t;
  if (eqz(v)) goto B_a;
  var w:int = e[3];
  var x:int = 0;
  var y:int = w;
  var z:int = x;
  var aa:int = y >= z;
  var ba:int = 0;
  var ca:int = 1;
  var da:int = aa & ca;
  n = ba;
  if (eqz(da)) goto B_a;
  var ea:int = e[2];
  var fa:int = 0;
  var ga:int = ea;
  var ha:int = fa;
  var ia:int = ga >= ha;
  n = ia;
  label B_a:
  var ja:int = n;
  var ka:int = 1;
  var la:int = ja & ka;
  return la;
}

export function checker(a:int, b:int, c:int):int {
  var d:int = g_a;
  var e:int = 32;
  var f:int = d - e;
  var g:int_ptr = f;
  g_a = f;
  g[7] = a;
  g[6] = b;
  g[5] = c;
  var h:int = g[5];
  var i:int = f;
  g[4] = i;
  var j:int = 2;
  var k:int = h << j;
  var l:int = 15;
  var m:int = k + l;
  var n:int = -16;
  var o:int = m & n;
  var p:int = f;
  var q:int_ptr = p - o;
  f = q;
  g_a = f;
  g[3] = h;
  var r:int = 0;
  g[2] = r;
  loop L_b {
    var s:int = g[2];
    var t:int = g[5];
    var u:int = s;
    var v:int = t;
    var w:int = u < v;
    var x:int = 1;
    var y:int = w & x;
    if (eqz(y)) goto B_a;
    var z:int = g[7];
    var aa:int = g[2];
    var ba:ubyte_ptr = z + aa;
    var ca:int = ba[0];
    var da:int = 24;
    var ea:int = ca << da;
    var fa:int = ea >> da;
    var ga:int = 48;
    var ha:int = fa - ga;
    var ia:int = g[2];
    var ja:int = 2;
    var ka:int = ia << ja;
    var la:int_ptr = q + ka;
    la[0] = ha;
    var ma:int = g[2];
    var na:int = 2;
    var oa:int = ma << na;
    var pa:int_ptr = q + oa;
    var qa:int = pa[0];
    var ra:int = 9;
    var sa:int = qa;
    var ta:int = ra;
    var ua:int = sa > ta;
    var va:int = 1;
    var wa:int = ua & va;
    if (eqz(wa)) goto B_c;
    var xa:int = g[2];
    var ya:int = 2;
    var za:int = xa << ya;
    var ab:int_ptr = q + za;
    var bb:int = ab[0];
    var cb:int = 39;
    var db:int = bb - cb;
    ab[0] = db;
    label B_c:
    var eb:int = g[2];
    var fb:int = 1;
    var gb:int = eb + fb;
    g[2] = gb;
    continue L_b;
  }
  unreachable;
  label B_a:
  var hb:int = g[5];
  var ib:int = 2;
  var jb:int = hb / ib;
  var kb:int = 2;
  var lb:int = jb << kb;
  var mb:int_ptr = q + lb;
  var nb:int = mb[0];
  var ob:int = 13;
  var pb:int = nb;
  var qb:int = ob;
  var rb:int = pb == qb;
  var sb:int = 0;
  var tb:int = 1;
  var ub:int = rb & tb;
  var vb:int = sb;
  if (eqz(ub)) goto B_d;
  var wb:int = g[5];
  var xb:int = 1;
  var yb:int = wb - xb;
  var zb:int = 2;
  var ac:int = yb << zb;
  var bc:int_ptr = q + ac;
  var cc:int = bc[0];
  var dc:int = f_d(cc);
  var ec:int = 0;
  var fc:int = 1;
  var gc:int = dc & fc;
  vb = ec;
  if (eqz(gc)) goto B_d;
  var hc:int = q[3];
  var ic:int = 1337;
  var jc:int = hc * ic;
  var kc:int = 100;
  var lc:int = jc + kc;
  var mc:int = f_c(lc);
  var nc:int = 0;
  var oc:int = 1;
  var pc:int = mc & oc;
  vb = nc;
  if (eqz(pc)) goto B_d;
  var qc:int = q[0];
  var rc:int = 6;
  var sc:int = qc;
  var tc:int = rc;
  var uc:int = sc > tc;
  var vc:int = 0;
  var wc:int = 1;
  var xc:int = uc & wc;
  vb = vc;
  if (eqz(xc)) goto B_d;
  var yc:int = q[0];
  var zc:int = 2;
  var ad:int = yc - zc;
  var bd:int = f_b(ad);
  var cd:int = 0;
  var dd:int = 1;
  var ed:int = bd & dd;
  vb = cd;
  if (eqz(ed)) goto B_d;
  var fd:int = q[1];
  var gd:int = q[6];
  var hd:int = f_e(fd, gd);
  var id:int = 0;
  var jd:int = 1;
  var kd:int = hd & jd;
  vb = id;
  if (eqz(kd)) goto B_d;
  var ld:int = q[5];
  var md:int = q[2];
  var nd:int = f_e(ld, md);
  var od:int = 0;
  var pd:int = 1;
  var qd:int = nd & pd;
  vb = od;
  if (eqz(qd)) goto B_d;
  var rd:int = q[1];
  var sd:int = q[2];
  var td:int = rd + sd;
  var ud:int = q[5];
  var vd:int = td + ud;
  var wd:int = q[6];
  var xd:int = vd + wd;
  var yd:int = q[1];
  var zd:int = 3;
  var ae:int = yd << zd;
  var be:int = xd;
  var ce:int = ae;
  var de:int = be == ce;
  var ee:int = 0;
  var fe:int = 1;
  var ge:int = de & fe;
  vb = ee;
  if (eqz(ge)) goto B_d;
  var he:int = q[5];
  var ie:int = q[6];
  var je:int = he;
  var ke:int = ie;
  var le:int = je >= ke;
  var me:int = 0;
  var ne:int = 1;
  var oe:int = le & ne;
  vb = me;
  if (eqz(oe)) goto B_d;
  var pe:int = q[5];
  var qe:int = q[6];
  var re:int = pe - qe;
  var se:int = 4;
  var te:int = re + se;
  var ue:int = f_b(te);
  var ve:int = 0;
  var we:int = 1;
  var xe:int = ue & we;
  vb = ve;
  if (eqz(xe)) goto B_d;
  var ye:int = q[1];
  var ze:int = q[2];
  var af:int = ye;
  var bf:int = ze;
  var cf:int = af > bf;
  var df:int = 0;
  var ef:int = 1;
  var ff:int = cf & ef;
  vb = df;
  if (eqz(ff)) goto B_d;
  var gf:int = q[1];
  var hf:int = q[2];
  var if:int = gf - hf;
  var jf:int = f_c(if);
  var kf:int = 0;
  var lf:int = 1;
  var mf:int = jf & lf;
  vb = kf;
  if (eqz(mf)) goto B_d;
  var nf:int = g[6];
  var of:int = f_g(nf);
  var pf:int = 3;
  var qf:int = of;
  var rf:int = pf;
  var sf:int = qf == rf;
  var tf:int = 0;
  var uf:int = 1;
  var vf:int = sf & uf;
  vb = tf;
  if (eqz(vf)) goto B_d;
  var wf:int = g[6];
  var xf:int = 65536;
  var yf:int = 3;
  var zf:int = f_h(wf, xf, yf);
  var ag:int = 0;
  var bg:int = zf;
  var cg:int = ag;
  var dg:int = bg == cg;
  vb = dg;
  label B_d:
  var eg:int = vb;
  var fg:int = g[4];
  f = fg;
  var gg:int = 1;
  var hg:int = eg & gg;
  var ig:int = 32;
  var jg:int = g + ig;
  g_a = jg;
  return hg;
}

function f_g(a:int):int {
  var c:int_ptr;
  var b:ubyte_ptr = a;
  if (eqz(a & 3)) goto B_b;
  b = a;
  loop L_c {
    if (eqz(b[0])) goto B_a;
    b = b + 1;
    if (b & 3) continue L_c;
  }
  label B_b:
  loop L_d {
    c = b;
    b = c + 4;
    var d:int = c[0];
    if (eqz(((d ^ -1) & d + -16843009) & -2139062144)) continue L_d;
  }
  loop L_e {
    b = c;
    c = b + 1;
    if (b[0]) continue L_e;
  }
  label B_a:
  return b - a;
}

function f_h(a:{ a:ubyte, b:ubyte }, b:ubyte_ptr, c:int):int {
  if (c) goto B_a;
  return 0;
  label B_a:
  var d:int = 0;
  var e:int = a.a;
  if (eqz(e)) goto B_b;
  loop L_d {
    var f:int = b[0];
    if (eqz(f)) goto B_c;
    c = c + -1;
    if (eqz(c)) goto B_c;
    if ((e & 255) != f) goto B_c;
    b = b + 1;
    e = a.b;
    a = a + 1;
    if (e) continue L_d;
    goto B_b;
  }
  unreachable;
  label B_c:
  d = e;
  label B_b:
  return (d & 255) - b[0];
}

function f_i(a:int) {
  g_b = a
}

function f_j():int {
  return g_b
}

export function stackSave():int {
  return g_a
}

export function stackRestore(a:int) {
  g_a = a
}

export function stackAlloc(a:int):int {
  var b:int = g_a - a & -16;
  g_a = b;
  return b;
}

export function emscripten_stack_get_current():int {
  return g_a
}

export function emscripten_stack_init() {
  g_d = 65536;
  g_c = 0 + 15 & -16;
}

export function emscripten_stack_get_free():int {
  return g_a - g_c
}

export function emscripten_stack_get_base():int {
  return g_d
}

export function emscripten_stack_get_end():int {
  return g_c
}

function f_s(a:int) {
}

function f(a:int) {
}

function f_u():int {
  f_s(65548);
  return 65552;
}

function f_v() {
  f(65548)
}

function f_w(a:int):int {
  return 1
}

function f_x(a:int) {
}

export function fflush(a:int):int {
  var c:int;
  var b:int;
  var d:int;
  if (a) goto B_a;
  b = 0;
  if (eqz(0[16389]:int)) goto B_b;
  b = fflush(0[16389]:int);
  label B_b:
  if (eqz(0[16389]:int)) goto B_c;
  b = fflush(0[16389]:int) | b;
  label B_c:
  a = f_u()[0]:int;
  if (eqz(a)) goto B_d;
  loop L_e {
    c = 0;
    if (a[19]:int < 0) goto B_f;
    c = f_w(a);
    label B_f:
    if (a[5]:int == a[7]:int) goto B_g;
    b = fflush(a) | b;
    label B_g:
    if (eqz(c)) goto B_h;
    f_x(a);
    label B_h:
    a = a[14]:int;
    if (a) continue L_e;
  }
  label B_d:
  f_v();
  return b;
  label B_a:
  c = 0;
  if (a[19]:int < 0) goto B_i;
  c = f_w(a);
  label B_i:
  if (a[5]:int == a[7]:int) goto B_l;
  call_indirect(a, 0, 0, a[9]:int);
  if (a[5]:int) goto B_l;
  b = -1;
  if (c) goto B_k;
  goto B_j;
  label B_l:
  b = a[1]:int;
  if (b == (d = a[2]:int)) goto B_m;
  call_indirect(a, i64_extend_i32_s(b - d), 1, a[10]:int);
  label B_m:
  b = 0;
  a[7]:int = 0;
  a[2]:long = 0L;
  a[1]:long@4 = 0L;
  if (eqz(c)) goto B_j;
  label B_k:
  f_x(a);
  label B_j:
  return b;
}

export function errno_location():int {
  return 65560
}