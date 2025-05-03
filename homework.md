# CS3317 Project3 Homework

## 1.

$$
R'(s, a, s') = 
\begin{cases}
R(s, a, s'), & \text{if } s \neq o \text{ and }  s' \in S \\
0, & \text{if } s = o \text{ or }  s' = o \\
\end{cases}
$$

$$
T'(s' \mid s, a) = 
\begin{cases}
\gamma \cdot T(s' \mid s, a), & \text{if } s \neq o \text{ and } s' \in S \\
1 - \gamma, & \text{if } s \neq o \text{ and } s' = o \\
1, & \text{if } s = o \text{ and } s' = o \\
0, & \text{if } s = o \text{ and } s' \neq o \\
\end{cases} \\
$$

**PROOF:**

The origin optimal value equation with discount factor is as following:
$$
V^*(s) = \max_{\pi} \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t, s_{t+1}) \mid s_0 = s \text{ and } \forall i, s_i \in S \right]
$$
After removing discount factor and introduce new transition function and reward function, the prime optimal value equation can be presented as following:
$$
\begin{align}
V'^*(s) &= \max_{\pi} \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} R'(s_t, a_t, s_{t+1}) \mid s_0 = s \right] \\
&= \max_{\pi} \mathbb{E}_{\pi} \left[ \gamma \cdot R(s_0, a_0, s_1) + \sum_{t=0}^{\infty} \gamma \cdot R(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S \right] + \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} R'(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 = o \right]
\end{align}
$$
The second component of the second row is zero, because according to the transition function, the state will be stuck in state $o$ and all of rewards are zero. Therefore we get following equation:
$$
\begin{align}
V'^*(s) &= \max_{\pi} \mathbb{E}_{\pi} \left[ \gamma \cdot R(s_0, a_0, s_1) + \sum_{t=0}^{\infty} \gamma \cdot R(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S \right] \\
&= \max_{\pi} \mathbb{E}_{\pi} \left[ \gamma \cdot R(s_0, a_0, s_1) + \gamma^2 \cdot R(s_1, a_1, s_2) + \sum_{t=2}^{\infty} \gamma^2 \cdot R(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S, s_2 \in S \right] + \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} R'(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S, s_2 = 0 \right]
\end{align}
$$
The second component of the second row is still zero. Iterating on this, we will get following equation:
$$
\begin{align}
V'^*(s) &= \max_{\pi} \mathbb{E}_{\pi} \left[ \gamma \cdot R(s_0, a_0, s_1) + \sum_{t=0}^{\infty} \gamma \cdot R(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S \right] \\
&= \max_{\pi} \mathbb{E}_{\pi} \left[ \gamma \cdot R(s_0, a_0, s_1) + \gamma^2 \cdot R(s_1, a_1, s_2) + \sum_{t=2}^{\infty} \gamma^2 \cdot R(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S, s_2 \in S \right] \\
&= \max_{\pi} \mathbb{E}_{\pi} \left[ \gamma \cdot R(s_0, a_0, s_1) + \gamma^2 \cdot R(s_1, a_1, s_2) + \gamma^3 \cdot R(s_2, a_2, s_3) + \sum_{t=3}^{\infty} \gamma^3 \cdot R(s_t, a_t, s_{t+1}) \mid s_0 = s, s_1 \in S, s_2 \in S, s_3 \in S \right]\\
&... \\
&= \max_{\pi} \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t, s_{t+1}) \mid \ s_0 = s \text{ and } \forall i, s_i \in S \right]
\end{align}
$$
Q.E.D.

## 2.

### 1.

Because the proof is too complex, I present my written proof.

![image-20250502153208343](/home/illusionary/图片/typora_used/image-20250502153208343.png)

Explanation: *The index indicates the position of the equation.*

1. By metric definition.
2. By metric definition.
3. By function $H(x)$ definition.
4. By function $H(x)$ definition.
5. Combine like terms and eliminate variables.
6. Because $\gamma < 1$ .
7. By absolute value inequality.
8. By maximum value inequality.
9. Combine two maximum.

The proof of Lemma $*$ is as following:

![image-20250502153834683](/home/illusionary/图片/typora_used/image-20250502153834683.png)

### 2.

<img src="/home/illusionary/图片/typora_used/image-20250502183755382.png" alt="image-20250502183755382" style="zoom:150%;" />