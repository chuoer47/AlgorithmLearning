# 归并排序

归并排序求逆序对

```c++
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e5+10;
int n,a[N],b[N],p[N];
int MOD = 99999997;

void work(int a[]){ // 离散化
    for (int i = 0; i < n; i ++ ) p[i] = i;
    sort(p,p+n,[&](int x,int y){
        if (a[x]==a[y]) return x<y;  // 这里要保证稳定性
       return  a[x]<a[y];
    });
    for (int i = 0; i < n; i ++ ) a[p[i]] = i;
}

int mergesort(int a[],int l,int r){
    if (l >= r) return 0;
    int mid = (l+r)>>1;
    int res = (mergesort(a,l,mid)+mergesort(a,mid+1,r))%MOD;
    int i = l,j = mid + 1,k = 0;
    while (i <= mid && j <= r){
        if (a[i]<=a[j]) p[k++] = a[i++];
        else p[k++] = a[j++],res = (res + mid - i + 1)%MOD; // 求逆序对的关键步骤
    }
    while (i<=mid) p[k++] = a[i++];
    while (j<=r) p[k++] = a[j++];
    for (int i = l,j=0; i <= r; i ++,j++ ) a[i] = p[j];
    return res;
}



int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ ) cin >> a[i];
    for (int i = 0; i < n; i ++ ) cin >> b[i];
    work(a);work(b);
    for (int i = 0; i < n; i ++ ) p[a[i]] = i;
    for (int i = 0; i < n; i ++ ) b[i] = p[b[i]];
    int res = mergesort(b,0,n-1);
    cout << res << endl;
    return 0;
}
// 链接：https://www.acwing.com/activity/content/code/content/8755043/
```



# 多路归并

谦虚数字模板

```c++
#include <iostream>
#include <cstring>
#include <algorithm>


using namespace std;
typedef long long LL;

const int N = 1e5+10,K = 110;
int n,k;
int s[K],p[K];
int ans[N];

int main()
{
    cin >> k >> n;
    for (int i = 1; i <= k; i ++ )  cin>> s[i];
    ans[0] = 1;
    memset(p, 0, sizeof p);
    for (int j = 1; j <= n; j ++ ){
        int res = 2e9;
        for (int i = 1; i <= k; i ++ ){
            res = min(res, ans[p[i]]*s[i]);
        }
        for (int i = 1; i <= k; i ++ ){
            if (res == ans[p[i]]*s[i]) p[i]++;
        }
        ans[j] = res;
    }
    for (int j = 1; j <= n; j ++ ){
        if (ans[j-1]==ans[j])  cout << ans[j-1]<< " " << ans[j] <<endl;
    }
    cout << ans[n] << endl;
    return 0;
}
// 链接：https://www.acwing.com/activity/content/code/content/8756543/
```

# 日期问题

求日期模板

```c++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int a[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

bool gapyear(int y){
    return (y%4==0 && y%100 !=0 || y%400==0);
}

int cal(int n){
    int y = n/10000;
    int m = n%10000/100;
    int d = n%10000%100;

    a[2] = gapyear(y)?29:28;

    while (m--) d+= a[m];
    while (y--) d+= gapyear(y)?366:365;
    return d;
}

int main()
{
    int a,b;
    while (cin >> a>> b){
        cout << abs(cal(a)-cal(b))+1 << endl;
    }
    return 0;
}

// 链接：https://www.acwing.com/activity/content/code/content/8757178/
```

# 并查集

朴素并查集模板

```c++
int fa[N];

int find(int x){
    if (fa[x]!=x) fa[x] = find(fa[x]); // 路径压缩
    return fa[x];
}

void merge(int x,int y){
    fa[find(x)] = find(y);
}
```

