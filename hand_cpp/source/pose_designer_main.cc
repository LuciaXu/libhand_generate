// Copyright (c) 2011, Marin Saric <marin.saric@gmail.com>
// All rights reserved.
//
// This file is a part of LibHand. LibHand is open-source software. You can
// redistribute it and/or modify it under the terms of the LibHand
// license. The LibHand license is the BSD license with an added clause that
// requires academic citation. You should have received a copy of the
// LibHand license (the license.txt file) along with LibHand. If not, see
// <http://www.libhand.org/>

# include <exception>
# include <iostream>

# include "printfstring.h"

# include "pose_designer.h"

using namespace std;
using namespace libhand;

int file_num;
bool save_all;

int main(int argc, char **argv) {
  PoseDesigner pose_designer;
  if (argc<2)
  {
    cout<<"n for not save, y for save"<<endl;
    return 0;
  }
  if (argc==2)
  {
   if (std::string(argv[1])=="-n")
   {save_all=0;}
   else if(std::string(argv[1])=="-y")
   {
    cout<<"need to enter the file start number, if you want save files."<<endl;
    return 0;
   }
   else
   {cout<<"n for not save, y for save"<<endl;
    return 0;
   }
  }
  if (argc ==3)
  {
    if (std::string(argv[1])=="-n")
     {save_all=0;}
    else if (std::string(argv[1])=="-y")
     {save_all =1;
      file_num=atoi(argv[2]);
     }
     else
     {cout<<"n for not save, y for save"<<endl;
    return 0;}
  }
  

  try {
    pose_designer.Setup(argc, argv);
    pose_designer.Run();
  } catch (const std::exception &e) {
    cerr << "Exception: " << e.what() << endl;
  }

  return 0;
}
