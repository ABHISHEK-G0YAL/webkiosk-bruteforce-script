#include <iostream>
#include <string>

using namespace std;

main()
{
    string pwd="";
    for(char i='A';i<='Z';i++){
        for(char j='A';j<='Z';j++){
            for(int k=1;k<=31;k++){
                for(int l=1;l<=12;l++){
                    for(int m=1997;m<=2001;m++){
                        pwd+=i;
                        pwd+=j;
                        if(k<=9){
                            pwd+='0';
                            pwd+=to_string(k);
                        }
                        else
                            pwd+=to_string(k);
                        if(l<=9){
                            pwd+='0';
                            pwd+=to_string(l);
                        }
                        else
                            pwd+=to_string(l);
                        pwd+=to_string(m);
                        cout<<pwd<<endl;
                        pwd="";
                    }
                }
            }
        }
    }
    return 0;
}
