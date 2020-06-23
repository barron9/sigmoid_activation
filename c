#include <vector>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>

using namespace std;


struct Connection
{
    double weight;
    double deltaWeight;
};

class Neuron;

typedef vector<Neuron> Layer;

class Neuron{
    public:
        Neuron(unsigned numOutputs, unsigned myIndex);
        void setOutputVal(double val) {m_outputVal = val;}
        double getOutputVal() const {return m_outputVal;}
        void feedForward(const Layer &prevLayer);
        void calcOutputGradients(double targetVal);
        void calcHiddenGradients(const Layer &nextLayer);
        void updateInputWeights(Layer &prevLayer);
    private:
        static double transferFunction(double x);
        static double transferFunctionDerivative(double x);
        static double randomWeight(void) {return rand() / double(RAND_MAX);}
        double sumDOW(const Layer &nextLayer) const;
        double m_outputVal;
        vector<Connection> m_outputWeights;
        unsigned m_myIndex;
        double m_gradient;
        static double eta;
        static double alpha;
};

int main()
{
int a=20,b=10,*p1=&a,*p2=&b;
cout<<"Before swap: *p1="<<*p1<<" *p2="<<*p2<<endl;
*p1=*p1 + *p2;
*p2=*p1 - *p2;
*p1=*p1 - *p2;
cout<<"After swap: *p1="<<*p1<<" *p2="<<*p2<<endl;
   return 0;
}
